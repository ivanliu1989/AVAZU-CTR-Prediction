# AVAZU CTR Prediction - Setup Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Project Structure](#project-structure)
4. [Quick Start](#quick-start)
5. [External Tools](#external-tools)
6. [Configuration](#configuration)
7. [Running Models](#running-models)
8. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Python Environment
- **Python 3.7+** (code is Python 2.7 legacy but migration to Python 3 recommended)
- pip or conda for package management
- virtualenv or venv for environment isolation

### R Environment (Optional)
- **R 4.0+**
- Required R packages: `h2o`, `FeatureHashing`, `caret`, `data.table`, `xgboost`

### System Requirements
- **RAM**: 16GB+ recommended (dataset is ~6GB uncompressed)
- **Storage**: 20GB+ free space
- **CPU**: Multi-core recommended for XGBoost/H2O

---

## Installation

### 1. Clone Repository
```bash
git clone <repository-url>
cd AVAZU-CTR-Prediction
```

### 2. Create Virtual Environment
```bash
# Using venv (Python 3)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Or using conda
conda create -n avazu python=3.8
conda activate avazu
```

### 3. Install Python Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install External Tools (Optional)

#### Vowpal Wabbit
```bash
# macOS
brew install vowpal-wabbit

# Ubuntu/Debian
sudo apt-get install vowpal-wabbit

# From source
git clone https://github.com/VowpalWabbit/vowpal_wabbit.git
cd vowpal_wabbit
make
sudo make install
```

#### XGBoost
```bash
pip install xgboost

# Or build from source for best performance
git clone --recursive https://github.com/dmlc/xgboost
cd xgboost
mkdir build && cd build
cmake ..
make -j4
cd ../python-package
python setup.py install
```

#### libFM
```bash
# Download from http://www.libfm.org/
wget http://www.libfm.org/libfm-1.42.src.tar.gz
tar -xzf libfm-1.42.src.tar.gz
cd libfm-1.42/
make all
# Add to PATH or copy binary to /usr/local/bin
```

#### H2O (for R)
```R
# In R console
install.packages("h2o")
```

---

## Project Structure

```
AVAZU-CTR-Prediction/
├── config.py                 # Centralized configuration
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore patterns
├── SETUP.md                 # This file
├── README.md                # Project overview
│
├── utils/                   # Utility modules
│   ├── __init__.py
│   └── logging_utils.py    # Logging utilities
│
├── models/                  # Refactored model implementations
│   ├── __init__.py
│   └── ftrl.py             # FTRL-Proximal (Python 3)
│
├── data/                    # Processed data (create this)
├── models_output/           # Trained models (create this)
├── pred/                    # Predictions (create this)
├── logs/                    # Log files (create this)
│
├── Python/                  # Original Python implementations
│   └── fast_solution_v*.py
│
├── Summary/                 # Production pipeline
│   ├── 1_preprocessing.py
│   ├── 2_split_app_site.py
│   ├── 3_feature_eng_*.py
│   ├── 4_*.py
│   └── 5_blending_models.py
│
├── MAIN_IMPROVE/           # Advanced experiments
│   └── *.py
│
└── [other directories...]
```

---

## Quick Start

### 1. Download Dataset
```bash
# Download from Kaggle (requires Kaggle API)
kaggle competitions download -c avazu-ctr-prediction

# Or download manually from:
# https://www.kaggle.com/c/avazu-ctr-prediction/data

# Extract to other/raw/
mkdir -p other/raw
unzip avazu-ctr-prediction.zip -d other/raw/
```

### 2. Run Preprocessing
```bash
# Method 1: Using new refactored code
python -c "from config import config; print(config.paths.data_dir)"

# Method 2: Using original pipeline
python Summary/1_preprocessing.py
python Summary/2_split_app_site.py
```

### 3. Train FTRL Model
```bash
# Using refactored implementation
python models/ftrl.py

# Or using original implementation
python Summary/4_ftrl_model.py
```

### 4. Train Other Models
```bash
# XGBoost
xgboost xgboost/xgboost_naive.R

# Vowpal Wabbit
python Summary/4_csv_2_vw.py
vw -d data/train.vw --loss_function logistic -b 28 -l 0.13 \
   -c -k --passes 15 -f model.vw

# H2O (in R)
Rscript R/CTR.R
```

### 5. Ensemble Predictions
```bash
python Summary/5_blending_models.py
```

---

## External Tools

### Vowpal Wabbit Commands
```bash
# Training
vw -d train.vw \
   --loss_function logistic \
   -b 28 \                     # 2^28 hash size
   -l 0.13 \                   # learning rate
   -c \                        # use cache
   -k \                        # kill cache on exit
   --passes 15 \               # number of passes
   -f model.vw \              # output model
   --holdout_period 100 \      # validation
   --l1 3e-9 \                # L1 regularization
   --l2 6e-9 \                # L2 regularization
   -q ad \                    # quadratic features
   --cubic aaa                # cubic features

# Prediction
vw test.vw -t -i model.vw -p predictions.txt
```

### XGBoost Configuration
Create `xgboost.conf`:
```
task = train
booster = gbtree
objective = binary:logistic
eta = 0.15
max_depth = 9
num_round = 900
eval_metric = logloss
data = train.libsvm
eval[test] = test.libsvm
model_out = xgboost.model
```

Run:
```bash
xgboost xgboost.conf
```

### libFM Commands
```bash
# MCMC method
libFM -task c \
      -train train.libsvm \
      -test test.libsvm \
      -out predictions.txt \
      -dim '1,1,8' \           # bias, 1-way, 2-way interactions
      -iter 900 \
      -method mcmc \
      -init_stdev 0.1

# SGD method
libFM -task c \
      -train train.libsvm \
      -test test.libsvm \
      -out predictions.txt \
      -dim '1,1,8' \
      -iter 100 \
      -method sgd \
      -learn_rate 0.01 \
      -regular '0,0,0.01'
```

---

## Configuration

### Editing Configuration
Edit `config.py` to customize:

```python
from config import Config

config = Config()

# Adjust FTRL parameters
config.ftrl.alpha = 0.15      # Increase learning rate
config.ftrl.L1 = 2.0          # Increase L1 regularization
config.ftrl.interaction = True # Enable feature interactions

# Adjust paths
config.paths.data_dir = '/custom/path/to/data'
```

### Environment Variables
```bash
export AVAZU_DATA_DIR=/path/to/data
export AVAZU_LOG_LEVEL=DEBUG
```

---

## Running Models

### FTRL (Python)
```python
from models.ftrl import FTRLProximal, train_ftrl
from config import config
from utils.logging_utils import setup_logger

# Setup logging
setup_logger('ftrl', log_file='logs/ftrl.log')

# Create learner
learner = FTRLProximal(
    alpha=config.ftrl.alpha,
    beta=config.ftrl.beta,
    L1=config.ftrl.L1,
    L2=config.ftrl.L2,
    D=config.ftrl.D,
    interaction=False
)

# Train
stats = train_ftrl(
    learner=learner,
    train_files=['data/train_df_site.csv', 'data/train_df_app.csv'],
    test_files=['data/test_df_site.csv', 'data/test_df_app.csv'],
    output_file='pred/ftrl_submission.csv'
)
```

### Complete Pipeline
```bash
# 1. Preprocess
python Summary/1_preprocessing.py
python Summary/2_split_app_site.py
python Summary/3_feature_eng_site.py
python Summary/3_feature_eng_app.py

# 2. Train models
python Summary/4_ftrl_model.py          # FTRL
xgboost 4_xgboost_site.conf            # XGBoost
python Summary/4_csv_2_vw.py           # Convert to VW format
vw -d train.vw ... -f model.vw         # Vowpal Wabbit

# 3. Blend predictions
python Summary/5_blending_models.py
```

---

## Troubleshooting

### Common Issues

#### 1. Python 2 vs Python 3
**Error**: `NameError: name 'xrange' is not defined`
**Solution**: Use Python 2.7 or migrate code:
```python
# Change:
for i in xrange(10):
# To:
for i in range(10):
```

#### 2. Memory Issues
**Error**: `MemoryError` or system slowdown
**Solutions**:
- Process data in chunks
- Reduce hash dimension: `D = 2 ** 24` instead of `2 ** 28`
- Use out-of-core processing
- Increase system swap

#### 3. File Not Found
**Error**: `FileNotFoundError: [Errno 2] No such file or directory`
**Solution**: Check paths in scripts or use `config.py`

#### 4. Missing Dependencies
**Error**: `ModuleNotFoundError: No module named 'xxx'`
**Solution**: Install missing package:
```bash
pip install xxx
```

### Performance Tips

1. **Use SSD storage** for faster I/O
2. **Enable multiprocessing** where applicable
3. **Use appropriate hash dimensions**:
   - Small datasets: 2^20 to 2^24
   - Medium datasets: 2^24 to 2^26
   - Large datasets: 2^26 to 2^28
4. **Tune learning rates** based on validation loss
5. **Use holdout validation** to monitor overfitting

### Getting Help

- Check logs in `logs/` directory
- Review configuration in `config.py`
- Consult original competition forum: https://www.kaggle.com/c/avazu-ctr-prediction/discussion
- Report issues on GitHub

---

## Next Steps

1. Read [ARCHITECTURE.md](ARCHITECTURE.md) for system design
2. Review [CODE_IMPROVEMENTS.md](CODE_IMPROVEMENTS.md) for enhancement details
3. Experiment with different hyperparameters
4. Try Python 3 migration using [PYTHON3_MIGRATION.md](PYTHON3_MIGRATION.md)
5. Implement additional ensemble strategies

---

**Last Updated**: 2025-01-27
