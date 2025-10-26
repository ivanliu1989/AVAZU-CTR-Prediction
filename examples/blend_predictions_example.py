#!/usr/bin/env python3
"""
Example: Blending multiple model predictions
============================================
This script demonstrates how to blend predictions from multiple models.

Usage:
    python examples/blend_predictions_example.py
"""
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.ensemble import blend_predictions
from utils.logging_utils import setup_logger


def main():
    """Main blending function"""

    # Setup logging
    logger = setup_logger(
        'blend_example',
        log_file='logs/blend_example.log'
    )

    logger.info("=" * 60)
    logger.info("Prediction Blending Example")
    logger.info("=" * 60)

    # Define prediction files
    # NOTE: Update these paths to match your actual prediction files
    prediction_files = [
        'pred/ftrl_submission.csv',
        'pred/xgboost_submission.csv',
        'pred/vw_cubic_submission.csv',
        'pred/vw_nn_submission.csv',
        'pred/libfm_submission.csv',
    ]

    output_file = 'pred/blended_submission.csv'

    logger.info(f"\nInput Prediction Files ({len(prediction_files)}):")
    for f in prediction_files:
        exists = "✓" if os.path.exists(f) else "✗ (missing)"
        logger.info(f"  {exists} {f}")

    # Check if files exist
    existing_files = [f for f in prediction_files if os.path.exists(f)]

    if len(existing_files) < 2:
        logger.error("\nNeed at least 2 prediction files to blend.")
        logger.error("Please train models first or update file paths in this script.")
        return 1

    # Try different blending methods
    methods = ['arithmetic', 'harmonic', 'geometric']

    for method in methods:
        logger.info(f"\n" + "-" * 60)
        logger.info(f"Blending with method: {method}")
        logger.info("-" * 60)

        method_output = output_file.replace('.csv', f'_{method}.csv')

        try:
            blended = blend_predictions(
                prediction_files=existing_files,
                output_file=method_output,
                method=method,
                calibration_shift=-0.005  # Apply calibration
            )

            # Compute statistics
            values = list(blended.values())
            avg_pred = sum(values) / len(values)
            min_pred = min(values)
            max_pred = max(values)

            logger.info(f"\n{method.capitalize()} Blending Results:")
            logger.info(f"  Number of predictions: {len(blended):,}")
            logger.info(f"  Average prediction: {avg_pred:.6f}")
            logger.info(f"  Min prediction: {min_pred:.6f}")
            logger.info(f"  Max prediction: {max_pred:.6f}")
            logger.info(f"  Output: {method_output}")

        except Exception as e:
            logger.error(f"Error with {method} blending: {e}")

    # Weighted blending example
    logger.info(f"\n" + "-" * 60)
    logger.info("Weighted Blending Example")
    logger.info("-" * 60)

    # Define weights (should sum to 1.0)
    # Weights based on individual model performance
    weights = [0.3, 0.25, 0.2, 0.15, 0.1][:len(existing_files)]
    # Normalize to sum to 1.0
    weight_sum = sum(weights)
    weights = [w / weight_sum for w in weights]

    logger.info(f"\nWeights:")
    for f, w in zip(existing_files, weights):
        logger.info(f"  {os.path.basename(f)}: {w:.3f}")

    weighted_output = output_file.replace('.csv', '_weighted.csv')

    try:
        blended = blend_predictions(
            prediction_files=existing_files,
            output_file=weighted_output,
            method='weighted',
            weights=weights,
            calibration_shift=-0.005
        )

        logger.info(f"\nWeighted Blending Results:")
        logger.info(f"  Output: {weighted_output}")
        logger.info(f"  Predictions: {len(blended):,}")

    except Exception as e:
        logger.error(f"Error with weighted blending: {e}")

    logger.info("\n" + "=" * 60)
    logger.info("Blending Complete!")
    logger.info("=" * 60)
    logger.info("\nRecommendation:")
    logger.info("  Compare blending methods on validation set")
    logger.info("  Typically harmonic mean works best for CTR prediction")

    return 0


if __name__ == '__main__':
    sys.exit(main())
