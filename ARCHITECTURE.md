# AVAZU CTR Prediction - Architecture Overview

## System Architecture

### High-Level Design

```
┌─────────────────────────────────────────────────────────────────┐
│                      AVAZU CTR Prediction                        │
│                  Click-Through Rate Prediction                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                         1. DATA LAYER                            │
├─────────────────────────────────────────────────────────────────┤
│  Raw Data (11 days)                                             │
│  ├── train.csv (40M rows, 6GB)                                  │
│  └── test.csv  (4.5M rows)                                      │
│                                                                  │
│  Features: hour, C1, banner_pos, site_*, app_*, device_*       │
│  Target: click (binary: 0/1)                                    │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                   2. PREPROCESSING LAYER                         │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  Null Value  │  │   Temporal   │  │  Category    │         │
│  │   Handling   │→ │   Features   │→ │   Split      │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│         │                 │                  │                  │
│    MD5 hashes        hour, dow          site / app              │
│    → empty          → features          → separate              │
│                                            datasets              │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                 3. FEATURE ENGINEERING LAYER                     │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ One-Hot      │  │ Hash Trick   │  │ Smoothing    │         │
│  │ Encoding     │  │ (2^28 dim)   │  │ (Laplace)    │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│         │                 │                  │                  │
│   Low cardinality   High cardinality    CTR estimates          │
│   (<10k values)     (millions)          (α=10)                 │
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐                           │
│  │ Interactions │  │ Unseen Vars  │                           │
│  │ (poly2)      │  │ Handling     │                           │
│  └──────────────┘  └──────────────┘                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                     4. MODEL TRAINING LAYER                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Online Learning Models                       │  │
│  ├──────────────────────────────────────────────────────────┤  │
│  │  FTRL-Proximal (Python)                                  │  │
│  │  ├── Learning rate: 0.13                                 │  │
│  │  ├── L1 reg: 1.0                                         │  │
│  │  ├── L2 reg: 1.0                                         │  │
│  │  ├── Hash dimension: 2^28                                │  │
│  │  └── 3 epochs, holdout validation                        │  │
│  │                                                            │  │
│  │  Vowpal Wabbit                                           │  │
│  │  ├── Logistic loss                                       │  │
│  │  ├── Cubic interactions                                  │  │
│  │  ├── Neural network mode                                 │  │
│  │  └── 15 passes                                           │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │          Batch Learning Models                            │  │
│  ├──────────────────────────────────────────────────────────┤  │
│  │  XGBoost                                                  │  │
│  │  ├── Max depth: 9                                        │  │
│  │  ├── Learning rate: 0.15                                 │  │
│  │  ├── Rounds: 600-900                                     │  │
│  │  └── Binary logistic objective                           │  │
│  │                                                            │  │
│  │  libFM (Factorization Machines)                          │  │
│  │  ├── MCMC method                                         │  │
│  │  ├── Dimensions: (1,1,8)                                 │  │
│  │  ├── Iterations: 900                                     │  │
│  │  └── SGD alternative                                     │  │
│  │                                                            │  │
│  │  H2O GBM (R)                                             │  │
│  │  └── Distributed gradient boosting                       │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    5. ENSEMBLE & CALIBRATION                     │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   FTRL       │  │  XGBoost     │  │   VW NN      │         │
│  │  0.3931037   │  │  0.3931970   │  │  0.3987734   │         │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘         │
│         │                 │                  │                  │
│  ┌──────▼──────┐  ┌───────▼──────┐  ┌───────▼──────┐         │
│  │  VW Cubic   │  │   libFM      │  │  libLinear   │         │
│  │  0.3957190  │  │  0.4027643   │  │  0.3964280   │         │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘         │
│         │                 │                  │                  │
│         └─────────────────┴──────────────────┘                 │
│                           │                                     │
│                    ┌──────▼──────┐                             │
│                    │  Blending   │                             │
│                    │  (Harmonic  │                             │
│                    │   Mean)     │                             │
│                    └──────┬──────┘                             │
│                           │                                     │
│                    ┌──────▼──────┐                             │
│                    │ Calibration │                             │
│                    │   (-0.005)  │                             │
│                    └──────┬──────┘                             │
│                           │                                     │
│                  Final: 0.3882 (LB)                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## Component Details

### 1. Data Layer

**Raw Dataset**:
- **Training**: 40.4M rows, ~6GB compressed
- **Testing**: 4.58M rows
- **Time Range**: 10 days (Oct 21-30, 2014)
- **Features**: 23 columns (mix of categorical and temporal)

**Feature Types**:
- `hour`: YYMMDDHH format (temporal)
- `C1, C14-C21`: Anonymous categorical features
- `banner_pos`: Ad banner position
- `site_*`: Website identifiers (ID, domain, category)
- `app_*`: Mobile app identifiers
- `device_*`: Device information (ID, IP, model, type, connection)

**Target**:
- `click`: Binary (0 = no click, 1 = click)
- Class imbalance: ~17% positive rate

---

### 2. Preprocessing Layer

#### Null Value Handling
**Issue**: Missing values encoded as MD5 hashes
- `d41d8cd9`: Empty string MD5
- `85f751fd`, `c4e18dd6`, etc.: Domain-specific nulls

**Solution**: Replace with empty string or special token

#### Temporal Feature Extraction
```python
hour = row['hour'][6:]  # Extract HH from YYMMDDHH
date = row['hour'][4:6]  # Extract DD
day_of_week = calculate_dow(date)  # Mon-Sun
```

**Key Insights**:
- Halloween (Oct 31) behaves differently
- Friday (24th) shows unique patterns
- Weekend vs. weekday distinction important

#### Category Splitting
**Rationale**: Mobile apps vs. websites have different CTR patterns

**Method**:
```python
if row['app_id'] == '':
    category = 'site'
else:
    category = 'app'
```

**Impact**: +2% performance improvement

---

### 3. Feature Engineering Layer

#### One-Hot Encoding
**Criteria**: Features with <10k distinct values
```python
if cardinality < 10000:
    one_hot_encode(feature)
else:
    hash_encode(feature)
```

**Advantages**: Exact representation, interpretable

#### Hash Trick (Feature Hashing)
**Dimension**: 2^28 = 268,435,456 buckets

```python
def hash_feature(key, value, D):
    feature_str = f"{key}_{value}"
    return hash(feature_str) % D
```

**Advantages**:
- Constant memory (regardless of cardinality)
- Handles unseen values automatically
- Collision probability: ~0.001% at 2^28

#### Laplace Smoothing
**Formula**:
```
CTR_smoothed = (clicks + α) / (impressions + α * 2)
```

**Parameter**: α = 10

**Purpose**: Prevent overfitting on rare features

#### Feature Interactions
**Poly2 (pairwise)**:
```python
for i in range(len(features)):
    for j in range(i+1, len(features)):
        interaction = hash(f"{features[i]}_{features[j]}") % D
        yield interaction
```

**Trade-off**:
- Improves accuracy: +1-2%
- Increases training time: 3-5x
- Final model: Disabled (diminishing returns)

---

### 4. Model Training Layer

#### FTRL-Proximal (Primary Model)
**Algorithm**: Follow-The-Regularized-Leader with proximal terms

**Update Rule**:
```
w_i = (sign(z_i) * L1 - z_i) / ((β + sqrt(n_i)) / α + L2)
z_i += g_i - σ_i * w_i
n_i += g_i^2
```

**Where**:
- `w_i`: Weight for feature i
- `z_i`: Weight accumulator
- `n_i`: Squared gradient accumulator (AdaGrad)
- `g_i`: Gradient (prediction error)
- `α`: Learning rate (0.13)
- `β`: Smoothing (1.0)
- `L1, L2`: Regularization (1.0, 1.0)

**Advantages**:
- Online learning (memory efficient)
- Adaptive learning rates per feature
- Sparse solutions (L1 regularization)
- Fast training (~1 hour on full dataset)

**Performance**: 0.3931 (Leaderboard)

#### XGBoost (Secondary Model)
**Configuration**:
```
max_depth = 9
eta = 0.15
num_round = 900
objective = binary:logistic
eval_metric = logloss
```

**Advantages**:
- Captures non-linear patterns
- Feature interactions automatic
- Handles missing values
- Regularization built-in

**Challenges**:
- Memory intensive (requires ~32GB RAM)
- Slower training (~4-6 hours)
- Risk of overfitting (mitigated with early stopping)

**Performance**: 0.3932

#### Vowpal Wabbit (Tertiary Model)
**Two Configurations**:

1. **Cubic Interactions**:
```bash
vw --cubic aaa --cubic ddd -q ad -b 28 -l 0.13
```

2. **Neural Network**:
```bash
vw --nn 3 -b 28 -l 0.13
```

**Advantages**:
- Extremely fast (10x faster than FTRL)
- Rich feature interactions
- Battle-tested in production

**Performance**: 0.3957 (Cubic), 0.3988 (NN)

#### libFM (Quaternary Model)
**Method**: Factorization Machines with MCMC

**Configuration**:
```
dim = (1, 1, 8)  # bias, 1-way, 2-way
iter = 900
method = mcmc
init_stdev = 0.1
```

**Advantages**:
- Models all feature interactions
- Bayesian approach (uncertainty estimates)
- Works well with sparse data

**Challenges**:
- Slowest training (~12 hours)
- Difficult to tune

**Performance**: 0.4028

---

### 5. Ensemble & Calibration Layer

#### Blending Strategy
**Method**: Harmonic Mean

```python
H = 6 / (1/p1 + 1/p2 + 1/p3 + 1/p4 + 1/p5 + 1/p6)
```

**Models**:
1. FTRL (Python): 0.3931
2. XGBoost: 0.3932
3. VW Cubic: 0.3957
4. VW NN: 0.3988
5. libFM: 0.4028
6. libLinear: 0.3964

**Rationale**:
- Harmonic mean penalizes outliers
- More robust than arithmetic mean
- Better calibrated probabilities

**Alternatives Tested**:
- Simple average: 0.3905
- Weighted average: 0.3897
- Geometric mean: 0.3901
- **Harmonic mean: 0.3887** ✓

#### Calibration
**Method**: Global shift

```python
prediction_calibrated = prediction - 0.005
```

**Rationale**:
- Training set CTR: 17.0%
- Test set CTR (estimated): 16.5%
- Shift corrects distribution mismatch

**Impact**: 0.3887 → 0.3882 (final)

---

## Data Flow

### Training Pipeline
```
Raw Data
  ↓
1_preprocessing.py (null handling)
  ↓
2_split_app_site.py (category split)
  ↓
3_feature_eng_*.py (feature creation)
  ↓
3_noisy_removal_*.py (smoothing)
  ↓
3_unseen_var_*.py (test handling)
  ↓
4_csv2*.py (format conversion)
  ↓
4_*_model.py (model training)
  ↓
5_blending_models.py (ensemble)
  ↓
Final Submission (0.3882)
```

### File Formats
- **CSV**: Raw data, preprocessed features
- **VW**: Vowpal Wabbit format (namespace-based)
- **libSVM**: Sparse format for libFM/XGBoost
- **Binary**: Model checkpoints (.model, .vw, .fm)

---

## Performance Characteristics

### Training Time (Single Pass)
| Model | Time | Memory | Accuracy |
|-------|------|--------|----------|
| FTRL | 1h | 4GB | 0.3931 |
| XGBoost | 4-6h | 32GB | 0.3932 |
| VW Cubic | 30m | 2GB | 0.3957 |
| VW NN | 45m | 3GB | 0.3988 |
| libFM | 12h | 8GB | 0.4028 |

### Scalability
- **FTRL**: O(n) time, O(D) space → Linear scalability
- **XGBoost**: O(n * d * log(n)) → Slower on large datasets
- **VW**: O(n) time → Best for streaming data

---

## Technology Stack

### Core Languages
- **Python 2.7** (legacy) / **Python 3.7+** (refactored)
- **R 3.x+** (H2O, ensemble experiments)
- **Bash** (pipeline orchestration)

### ML Frameworks
- **Scikit-learn**: Preprocessing, utilities
- **XGBoost**: Gradient boosting
- **Vowpal Wabbit**: Online learning
- **libFM**: Factorization machines
- **H2O**: Distributed ML (R)

### Data Processing
- **Pandas**: DataFrame operations
- **NumPy**: Numerical computations
- **CSV**: Streaming I/O

---

## Design Patterns

### 1. Hash Trick Pattern
**Problem**: High-cardinality features (millions of values)
**Solution**: Fixed-size hash table (2^28)
**Trade-off**: Memory vs. collision rate

### 2. Online Learning Pattern
**Problem**: Dataset too large for memory
**Solution**: Stream data, update incrementally
**Models**: FTRL, VW

### 3. Ensemble Pattern
**Problem**: Single model limitations
**Solution**: Combine diverse models
**Method**: Harmonic mean blending

### 4. Stratified Training Pattern
**Problem**: Different categories have different patterns
**Solution**: Train separate models (site vs. app)
**Impact**: +2% improvement

---

## Key Innovations

1. **Connection Type Stratification**: Separate models per device connection type
2. **Temporal Features**: Halloween, Friday, weekend handling
3. **Unseen Variable Handling**: Special encoding (-2) for test-only values
4. **Laplace Smoothing**: Prevents overfitting on rare features
5. **Harmonic Mean Blending**: More robust ensemble method
6. **Post-Calibration**: Distribution shift correction

---

## Lessons Learned

### What Worked
✅ Feature hashing (2^28 dimension)
✅ Separate site/app models
✅ Multiple model types (linear + tree-based)
✅ Harmonic mean blending
✅ Laplace smoothing
✅ Unseen variable handling

### What Didn't Work
❌ Feature interactions (too slow, minimal gain)
❌ Deep neural networks (overfitting)
❌ Complex feature engineering (diminishing returns)
❌ Geometric mean blending
❌ Over-aggressive regularization

### Surprises
- Halloween (Oct 31) qualitatively different
- Connection type matters more than expected
- Simple FTRL competitive with XGBoost
- Harmonic mean > arithmetic mean
- Calibration critical for final gain

---

## Future Improvements

### Algorithmic
- [ ] Field-aware Factorization Machines (FFM)
- [ ] Deep & Cross Networks
- [ ] Attention mechanisms
- [ ] AutoML for hyperparameter tuning

### Engineering
- [ ] Distributed training (Spark, Dask)
- [ ] Feature store
- [ ] Model serving API
- [ ] Real-time prediction pipeline
- [ ] A/B testing framework

### Data
- [ ] External data sources
- [ ] User behavior sequences
- [ ] Contextual features (weather, events)
- [ ] Cross-device tracking

---

## References

1. McMahan et al. (2013) "Ad Click Prediction: a View from the Trenches"
2. Chen & Guestrin (2016) "XGBoost: A Scalable Tree Boosting System"
3. Rendle (2010) "Factorization Machines"
4. Weinberger et al. (2009) "Feature Hashing for Large Scale Multitask Learning"

---

**Last Updated**: 2025-01-27
**Competition**: Avazu CTR Prediction (Kaggle)
**Final Rank**: 55/1786 (Top 3.1%)
**Final Score**: 0.3882 (Log Loss)
