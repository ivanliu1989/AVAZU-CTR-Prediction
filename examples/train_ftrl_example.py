#!/usr/bin/env python3
"""
Example: Training FTRL model on AVAZU data
==========================================
This script demonstrates how to use the refactored FTRL implementation.

Usage:
    python examples/train_ftrl_example.py
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.ftrl import FTRLProximal, train_ftrl
from config import config
from utils.logging_utils import setup_logger


def main():
    """Main training function"""

    # Setup logging
    logger = setup_logger(
        'ftrl_example',
        log_file='logs/ftrl_example.log'
    )

    logger.info("=" * 60)
    logger.info("FTRL Training Example")
    logger.info("=" * 60)

    # Configure model
    logger.info("\nModel Configuration:")
    logger.info(f"  Learning rate (alpha): {config.ftrl.alpha}")
    logger.info(f"  L1 regularization: {config.ftrl.L1}")
    logger.info(f"  L2 regularization: {config.ftrl.L2}")
    logger.info(f"  Hash dimension (D): {config.ftrl.D:,}")
    logger.info(f"  Feature interactions: {config.ftrl.interaction}")
    logger.info(f"  Epochs: {config.ftrl.epochs}")

    # Create learner
    learner = FTRLProximal(
        alpha=config.ftrl.alpha,
        beta=config.ftrl.beta,
        L1=config.ftrl.L1,
        L2=config.ftrl.L2,
        D=config.ftrl.D,
        interaction=config.ftrl.interaction
    )

    # Define data files
    # NOTE: Update these paths to match your actual data location
    train_files = [
        'data/train_df_site_processed.csv',
        'data/train_df_app_processed.csv'
    ]

    test_files = [
        'data/test_df_site_processed.csv',
        'data/test_df_app_processed.csv'
    ]

    output_file = config.get_submission_path('ftrl')

    logger.info(f"\nData Files:")
    logger.info(f"  Training: {len(train_files)} files")
    for f in train_files:
        logger.info(f"    - {f}")
    logger.info(f"  Testing: {len(test_files)} files")
    for f in test_files:
        logger.info(f"    - {f}")
    logger.info(f"  Output: {output_file}")

    # Check if files exist
    all_files = train_files + test_files
    missing_files = [f for f in all_files if not os.path.exists(f)]

    if missing_files:
        logger.error("\nMissing data files:")
        for f in missing_files:
            logger.error(f"  - {f}")
        logger.error("\nPlease run preprocessing first or update file paths in this script.")
        return 1

    # Train model
    logger.info("\n" + "=" * 60)
    logger.info("Starting Training...")
    logger.info("=" * 60 + "\n")

    try:
        stats = train_ftrl(
            learner=learner,
            train_files=train_files,
            test_files=test_files,
            output_file=output_file,
            epochs=config.ftrl.epochs,
            holdout_interval=config.ftrl.holdout_interval,
            log_interval=config.model.log_interval
        )

        # Print results
        logger.info("\n" + "=" * 60)
        logger.info("Training Complete!")
        logger.info("=" * 60)
        logger.info(f"\nFinal Validation Loss: {stats['final_loss']:.6f}")
        logger.info(f"Output file: {output_file}")
        logger.info("\nEpoch Summary:")
        for epoch_stats in stats['epochs']:
            logger.info(f"  Epoch {epoch_stats['epoch']}: Loss = {epoch_stats['loss']:.6f}")

        return 0

    except Exception as e:
        logger.error(f"\nTraining failed: {e}", exc_info=True)
        return 1


if __name__ == '__main__':
    sys.exit(main())
