"""
Configuration Management for AVAZU CTR Prediction
==================================================
Centralized configuration to avoid hardcoded paths and magic numbers.

Usage:
    from config import Config, Paths, FTRLConfig, XGBoostConfig

    config = Config()
    print(config.paths.data_dir)
"""
import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Paths:
    """File paths configuration"""
    # Base directories
    project_root: str = os.path.dirname(os.path.abspath(__file__))
    data_dir: str = os.path.join(project_root, 'data')
    raw_dir: str = os.path.join(project_root, 'other', 'raw')
    pred_dir: str = os.path.join(project_root, 'pred')
    model_dir: str = os.path.join(project_root, 'models')

    # Raw data files
    train_raw: str = os.path.join(raw_dir, 'train.csv')
    test_raw: str = os.path.join(raw_dir, 'test.csv')

    def __post_init__(self):
        """Create directories if they don't exist"""
        for directory in [self.data_dir, self.raw_dir, self.pred_dir, self.model_dir]:
            os.makedirs(directory, exist_ok=True)


@dataclass
class FTRLConfig:
    """FTRL-Proximal algorithm configuration"""
    # Learning parameters
    alpha: float = 0.13  # Learning rate
    beta: float = 1.0    # Smoothing parameter for adaptive learning rate
    L1: float = 1.0      # L1 regularization (larger = more regularized)
    L2: float = 1.0      # L2 regularization (larger = more regularized)

    # Feature hashing
    D: int = 2 ** 28     # Number of weights (268,435,456)
    interaction: bool = False  # Enable poly2 feature interactions

    # Training
    epochs: int = 3      # Number of passes through training data
    holdout_interval: Optional[int] = 100000  # Validation every N samples
    holdafter: Optional[int] = None  # Date threshold for validation split


@dataclass
class XGBoostConfig:
    """XGBoost configuration"""
    max_depth: int = 9
    eta: float = 0.15  # Learning rate
    num_rounds: int = 900
    objective: str = 'binary:logistic'
    eval_metric: str = 'logloss'


@dataclass
class PreprocessingConfig:
    """Data preprocessing configuration"""
    # Null value indicators (MD5 hashes)
    null_values: list = None

    # Feature engineering
    laplace_alpha: float = 10.0  # Smoothing parameter
    min_feature_count: int = 5   # Minimum occurrences to keep feature

    # Date ranges
    train_start_date: str = '14-10-21'
    train_end_date: str = '14-10-30'

    def __post_init__(self):
        if self.null_values is None:
            self.null_values = [
                'd41d8cd9',  # Empty MD5 hash
                '85f751fd',  # Missing site_id
                'c4e18dd6',  # Missing site_domain
                '50e219e0',  # Missing site_category
                'ecad2386',  # Missing app_id
                '7801e8d9',  # Missing app_domain
                '07d7df22',  # Missing app_category
            ]


@dataclass
class ModelConfig:
    """General model configuration"""
    random_seed: int = 42
    log_interval: int = 2500000  # Progress logging interval
    chunk_size: int = 100000     # Chunk size for data processing


class Config:
    """
    Main configuration class combining all configs

    Usage:
        config = Config()
        learner = ftrl_proximal(
            alpha=config.ftrl.alpha,
            beta=config.ftrl.beta,
            L1=config.ftrl.L1,
            L2=config.ftrl.L2,
            D=config.ftrl.D,
            interaction=config.ftrl.interaction
        )
    """
    def __init__(self):
        self.paths = Paths()
        self.ftrl = FTRLConfig()
        self.ftrl_site = FTRLConfig(alpha=0.13, L1=1.0, L2=1.0)
        self.ftrl_app = FTRLConfig(alpha=0.13, L1=1.0, L2=1.0)
        self.xgboost = XGBoostConfig()
        self.preprocessing = PreprocessingConfig()
        self.model = ModelConfig()

    def get_data_path(self, category: str, split: str, processed: bool = False) -> str:
        """
        Get standardized data file path

        Args:
            category: 'site' or 'app'
            split: 'train' or 'test'
            processed: If True, returns processed file path

        Returns:
            Full path to data file
        """
        suffix = '_processed' if processed else ''
        filename = f"{split}_df_{category}{suffix}.csv"
        return os.path.join(self.paths.data_dir, filename)

    def get_submission_path(self, model_name: str) -> str:
        """
        Get standardized submission file path

        Args:
            model_name: Name of the model (e.g., 'ftrl', 'xgboost')

        Returns:
            Full path to submission file
        """
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"submission_{model_name}_{timestamp}.csv"
        return os.path.join(self.paths.pred_dir, filename)


# Singleton instance for easy import
config = Config()


if __name__ == '__main__':
    # Example usage and configuration display
    cfg = Config()
    print("=" * 60)
    print("AVAZU CTR Prediction - Configuration")
    print("=" * 60)
    print(f"\nProject Root: {cfg.paths.project_root}")
    print(f"Data Directory: {cfg.paths.data_dir}")
    print(f"\nFTRL Configuration:")
    print(f"  Alpha (Learning Rate): {cfg.ftrl.alpha}")
    print(f"  L1 Regularization: {cfg.ftrl.L1}")
    print(f"  L2 Regularization: {cfg.ftrl.L2}")
    print(f"  Hash Size (D): {cfg.ftrl.D:,}")
    print(f"  Feature Interactions: {cfg.ftrl.interaction}")
    print(f"\nXGBoost Configuration:")
    print(f"  Max Depth: {cfg.xgboost.max_depth}")
    print(f"  Learning Rate (eta): {cfg.xgboost.eta}")
    print(f"  Rounds: {cfg.xgboost.num_rounds}")
    print("\n" + "=" * 60)
