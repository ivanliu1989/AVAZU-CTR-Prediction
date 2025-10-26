"""
FTRL-Proximal Algorithm Implementation
=======================================
Follow-The-Regularized-Leader (FTRL) with proximal terms for online learning.

This is a refactored, Python 3 compatible version with:
- Type hints
- Proper error handling
- Logging support
- Configuration management
- Code documentation

Reference:
    McMahan et al. (2013) "Ad Click Prediction: a View from the Trenches"
    https://research.google.com/pubs/pub41159.html

Usage:
    from models.ftrl import FTRLProximal, train_ftrl
    from config import config

    learner = FTRLProximal(
        alpha=config.ftrl.alpha,
        beta=config.ftrl.beta,
        L1=config.ftrl.L1,
        L2=config.ftrl.L2,
        D=config.ftrl.D,
        interaction=config.ftrl.interaction
    )

    train_ftrl(learner, 'data/train.csv', 'data/test.csv', 'output.csv')
"""
import csv
import logging
from typing import List, Dict, Tuple, Optional, Iterator
from math import exp, log, sqrt

logger = logging.getLogger(__name__)


class FTRLProximal:
    """
    FTRL-Proximal algorithm for online learning

    This implementation uses the hash trick for feature hashing and supports
    feature interactions.

    Attributes:
        alpha: Learning rate
        beta: Smoothing parameter for adaptive learning
        L1: L1 regularization strength
        L2: L2 regularization strength
        D: Dimension of feature space (typically 2^28)
        interaction: Whether to generate 2-way feature interactions
        n: Adaptive learning rate accumulator
        z: Weight accumulator
        w: Current weights (cached)
    """

    def __init__(
        self,
        alpha: float = 0.13,
        beta: float = 1.0,
        L1: float = 1.0,
        L2: float = 1.0,
        D: int = 2 ** 28,
        interaction: bool = False
    ):
        """
        Initialize FTRL-Proximal learner

        Args:
            alpha: Learning rate (typically 0.1-0.2)
            beta: Smoothing parameter for adaptive learning rate
            L1: L1 regularization (sparse weights)
            L2: L2 regularization (prevents overfitting)
            D: Hash space dimension (power of 2, e.g., 2^28)
            interaction: Enable 2-way feature interactions
        """
        self.alpha = alpha
        self.beta = beta
        self.L1 = L1
        self.L2 = L2
        self.D = D
        self.interaction = interaction

        # Model state
        self.n = [0.0] * D  # Squared gradient accumulator
        self.z = [0.0] * D  # Weight accumulator
        self.w = {}         # Current weights (computed on-demand)

    def _indices(self, x: List[int]) -> Iterator[int]:
        """
        Generate feature indices including bias and interactions

        Args:
            x: List of feature indices

        Yields:
            Feature indices (including bias term and interactions)
        """
        # Bias term
        yield 0

        # Original features
        for index in x:
            yield index

        # Feature interactions (if enabled)
        if self.interaction:
            x_sorted = sorted(x)
            n_features = len(x_sorted)

            for i in range(n_features):
                for j in range(i + 1, n_features):
                    # Hash the interaction
                    interaction_key = f"{x_sorted[i]}_{x_sorted[j]}"
                    yield hash(interaction_key) % self.D

    def predict(self, x: List[int]) -> float:
        """
        Predict probability for given features

        Args:
            x: List of feature indices

        Returns:
            Predicted probability (0-1)
        """
        # Compute weights with L1/L2 regularization
        w = {}
        wTx = 0.0

        for i in self._indices(x):
            sign = -1.0 if self.z[i] < 0 else 1.0

            # Apply L1 regularization (creates sparsity)
            if sign * self.z[i] <= self.L1:
                w[i] = 0.0
            else:
                # Compute weight with L1 and L2 regularization
                w[i] = (sign * self.L1 - self.z[i]) / (
                    (self.beta + sqrt(self.n[i])) / self.alpha + self.L2
                )

            wTx += w[i]

        # Cache weights for update step
        self.w = w

        # Bounded sigmoid to prevent overflow
        return self._sigmoid(wTx)

    def update(self, x: List[int], p: float, y: float):
        """
        Update model weights based on prediction and true label

        Args:
            x: List of feature indices
            p: Predicted probability
            y: True label (0 or 1)
        """
        # Gradient under log loss
        g = p - y

        # Update weights using FTRL update rule
        for i in self._indices(x):
            # Update per-coordinate learning rate
            sigma = (sqrt(self.n[i] + g * g) - sqrt(self.n[i])) / self.alpha

            # Update weight accumulators
            self.z[i] += g - sigma * self.w[i]
            self.n[i] += g * g

    @staticmethod
    def _sigmoid(x: float, clip: float = 35.0) -> float:
        """
        Bounded sigmoid function to prevent overflow

        Args:
            x: Input value
            clip: Clipping threshold

        Returns:
            Sigmoid value in (0, 1)
        """
        x_clipped = max(min(x, clip), -clip)
        return 1.0 / (1.0 + exp(-x_clipped))


def logloss(p: float, y: float, eps: float = 1e-15) -> float:
    """
    Compute log loss for a single prediction

    Args:
        p: Predicted probability
        y: True label (0 or 1)
        eps: Small constant to avoid log(0)

    Returns:
        Log loss value
    """
    p_clipped = max(min(p, 1.0 - eps), eps)
    return -log(p_clipped) if y == 1.0 else -log(1.0 - p_clipped)


def load_data(
    file_path: str,
    D: int,
    has_label: bool = True
) -> Iterator[Tuple[int, str, List[int], float]]:
    """
    Load data from CSV file with hash-based feature encoding

    Args:
        file_path: Path to CSV file
        D: Hash space dimension
        has_label: Whether file contains 'click' label column

    Yields:
        Tuple of (row_number, id, feature_indices, label)
    """
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)

            for t, row in enumerate(reader):
                # Extract ID
                row_id = row.pop('id')

                # Extract label (if present)
                y = 0.0
                if has_label and 'click' in row:
                    y = 1.0 if row.pop('click') == '1' else 0.0

                # Hash features
                x = []
                for key, value in row.items():
                    # Create feature string and hash it
                    feature_str = f"{key}_{value}"
                    index = hash(feature_str) % D
                    x.append(index)

                yield t, row_id, x, y

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")
        raise


def train_ftrl(
    learner: FTRLProximal,
    train_files: List[str],
    test_files: List[str],
    output_file: str,
    epochs: int = 3,
    holdout_interval: Optional[int] = 100000,
    log_interval: int = 2500000
) -> Dict[str, float]:
    """
    Train FTRL model and generate predictions

    Args:
        learner: FTRLProximal instance
        train_files: List of training file paths
        test_files: List of test file paths (must match train_files order)
        output_file: Path to output submission file
        epochs: Number of training epochs
        holdout_interval: Validation holdout interval (None = no validation)
        log_interval: Progress logging interval

    Returns:
        Dictionary with training statistics
    """
    from datetime import datetime

    stats = {'epochs': [], 'final_loss': 0.0}

    logger.info(f"Starting FTRL training with {len(train_files)} datasets")
    start_time = datetime.now()

    # Train on each dataset
    for train_file in train_files:
        logger.info(f"Training on: {train_file}")

        for epoch in range(epochs):
            epoch_start = datetime.now()
            loss_sum = 0.0
            count = 0

            try:
                for t, row_id, x, y in load_data(train_file, learner.D, has_label=True):
                    # Predict
                    p = learner.predict(x)

                    # Holdout validation
                    if holdout_interval and t % holdout_interval == 0:
                        loss_sum += logloss(p, y)
                        count += 1
                    else:
                        # Update model
                        learner.update(x, p, y)

                    # Progress logging
                    if t > 0 and t % log_interval == 0:
                        avg_loss = loss_sum / count if count > 0 else 0.0
                        logger.info(
                            f"  Row {t:,} | Validation Loss: {avg_loss:.6f} | "
                            f"Elapsed: {datetime.now() - epoch_start}"
                        )

                # Epoch summary
                avg_loss = loss_sum / count if count > 0 else 0.0
                epoch_time = datetime.now() - epoch_start

                logger.info(
                    f"Epoch {epoch + 1}/{epochs} | "
                    f"Validation Loss: {avg_loss:.6f} | "
                    f"Time: {epoch_time}"
                )

                stats['epochs'].append({'epoch': epoch + 1, 'loss': avg_loss})
                stats['final_loss'] = avg_loss

            except Exception as e:
                logger.error(f"Error during training: {e}", exc_info=True)
                raise

    # Generate predictions
    logger.info(f"Generating predictions -> {output_file}")

    try:
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'click'])

            for test_file in test_files:
                logger.info(f"Predicting on: {test_file}")

                for t, row_id, x, y in load_data(test_file, learner.D, has_label=False):
                    p = learner.predict(x)
                    writer.writerow([row_id, f"{p:.10f}"])

    except Exception as e:
        logger.error(f"Error writing predictions: {e}", exc_info=True)
        raise

    total_time = datetime.now() - start_time
    logger.info(f"Training completed in {total_time}")

    return stats


if __name__ == '__main__':
    # Example usage
    from utils.logging_utils import setup_logger

    setup_logger('ftrl', log_file='logs/ftrl_training.log')

    # Create learner
    learner = FTRLProximal(
        alpha=0.13,
        beta=1.0,
        L1=1.0,
        L2=1.0,
        D=2 ** 28,
        interaction=False
    )

    # Train (example paths - update with actual paths)
    stats = train_ftrl(
        learner=learner,
        train_files=['data/train_df_site.csv', 'data/train_df_app.csv'],
        test_files=['data/test_df_site.csv', 'data/test_df_app.csv'],
        output_file='predictions/ftrl_submission.csv',
        epochs=3,
        holdout_interval=100000
    )

    print(f"Final validation loss: {stats['final_loss']:.6f}")
