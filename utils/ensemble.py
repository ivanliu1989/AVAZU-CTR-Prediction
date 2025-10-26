"""
Ensemble and Blending Utilities for AVAZU CTR Prediction
=========================================================
Functions for combining multiple model predictions.

Usage:
    from utils.ensemble import blend_predictions, harmonic_mean, calibrate_predictions

    blended = blend_predictions(predictions, method='harmonic')
    calibrated = calibrate_predictions(blended, shift=-0.005)
"""
import csv
import logging
from typing import List, Dict, Optional
import math

logger = logging.getLogger(__name__)


def load_predictions(file_path: str) -> Dict[str, float]:
    """
    Load predictions from CSV file

    Args:
        file_path: Path to prediction CSV file

    Returns:
        Dictionary mapping ID to prediction probability
    """
    predictions = {}

    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                row_id = row['id']
                pred = float(row['click'])
                predictions[row_id] = pred

        logger.info(f"Loaded {len(predictions)} predictions from {file_path}")
        return predictions

    except FileNotFoundError:
        logger.error(f"Prediction file not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error loading predictions: {e}")
        raise


def arithmetic_mean(values: List[float]) -> float:
    """
    Compute arithmetic mean

    Args:
        values: List of values

    Returns:
        Arithmetic mean
    """
    if not values:
        return 0.0
    return sum(values) / len(values)


def harmonic_mean(values: List[float], epsilon: float = 1e-10) -> float:
    """
    Compute harmonic mean

    Args:
        values: List of values
        epsilon: Small value to avoid division by zero

    Returns:
        Harmonic mean
    """
    if not values:
        return 0.0

    # Add epsilon to avoid division by zero
    safe_values = [max(v, epsilon) for v in values]

    n = len(safe_values)
    reciprocal_sum = sum(1.0 / v for v in safe_values)

    return n / reciprocal_sum


def geometric_mean(values: List[float], epsilon: float = 1e-10) -> float:
    """
    Compute geometric mean

    Args:
        values: List of values
        epsilon: Small value to avoid log(0)

    Returns:
        Geometric mean
    """
    if not values:
        return 0.0

    # Add epsilon to avoid log(0)
    safe_values = [max(v, epsilon) for v in values]

    n = len(safe_values)
    log_sum = sum(math.log(v) for v in safe_values)

    return math.exp(log_sum / n)


def weighted_average(values: List[float], weights: List[float]) -> float:
    """
    Compute weighted average

    Args:
        values: List of values
        weights: List of weights (must sum to 1.0)

    Returns:
        Weighted average
    """
    if not values or not weights or len(values) != len(weights):
        raise ValueError("Values and weights must have same non-zero length")

    return sum(v * w for v, w in zip(values, weights))


def rank_average(predictions_list: List[Dict[str, float]]) -> Dict[str, float]:
    """
    Compute rank-based ensemble

    Args:
        predictions_list: List of prediction dictionaries

    Returns:
        Dictionary of averaged ranks converted back to probabilities
    """
    if not predictions_list:
        return {}

    # Get all IDs
    all_ids = set()
    for preds in predictions_list:
        all_ids.update(preds.keys())

    result = {}

    for row_id in all_ids:
        # Get predictions for this ID from all models
        values = []
        for preds in predictions_list:
            if row_id in preds:
                values.append(preds[row_id])

        if values:
            # Simple average of available predictions
            result[row_id] = arithmetic_mean(values)

    return result


def blend_predictions(
    prediction_files: List[str],
    output_file: str,
    method: str = 'harmonic',
    weights: Optional[List[float]] = None,
    calibration_shift: float = 0.0
) -> Dict[str, float]:
    """
    Blend multiple prediction files

    Args:
        prediction_files: List of paths to prediction CSV files
        output_file: Path to output blended predictions
        method: Blending method ('arithmetic', 'harmonic', 'geometric', 'weighted')
        weights: Weights for weighted average (must sum to 1.0)
        calibration_shift: Shift to apply after blending (e.g., -0.005)

    Returns:
        Dictionary of blended predictions
    """
    logger.info(f"Blending {len(prediction_files)} prediction files using {method} method")

    # Load all predictions
    all_predictions = []
    for file_path in prediction_files:
        preds = load_predictions(file_path)
        all_predictions.append(preds)

    # Get all IDs (should be same across all files)
    all_ids = set(all_predictions[0].keys())
    for preds in all_predictions[1:]:
        if set(preds.keys()) != all_ids:
            logger.warning("Prediction files have different ID sets!")
            all_ids = all_ids.intersection(set(preds.keys()))

    logger.info(f"Blending predictions for {len(all_ids)} IDs")

    # Blend predictions
    blended = {}

    for row_id in all_ids:
        values = [preds[row_id] for preds in all_predictions]

        if method == 'arithmetic':
            pred = arithmetic_mean(values)
        elif method == 'harmonic':
            pred = harmonic_mean(values)
        elif method == 'geometric':
            pred = geometric_mean(values)
        elif method == 'weighted':
            if weights is None or len(weights) != len(values):
                raise ValueError("Weights must be provided and match number of models")
            pred = weighted_average(values, weights)
        else:
            raise ValueError(f"Unknown blending method: {method}")

        # Apply calibration
        pred = pred + calibration_shift

        # Clip to valid probability range
        pred = max(min(pred, 1.0 - 1e-15), 1e-15)

        blended[row_id] = pred

    # Write output
    try:
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'click'])

            for row_id in sorted(blended.keys()):
                writer.writerow([row_id, f"{blended[row_id]:.10f}"])

        logger.info(f"Blended predictions written to {output_file}")

    except Exception as e:
        logger.error(f"Error writing blended predictions: {e}")
        raise

    return blended


def calibrate_predictions(
    predictions: Dict[str, float],
    shift: float = 0.0,
    scale: float = 1.0
) -> Dict[str, float]:
    """
    Calibrate predictions with shift and scale

    Args:
        predictions: Dictionary of predictions
        shift: Additive shift (e.g., -0.005)
        scale: Multiplicative scale (e.g., 0.95)

    Returns:
        Dictionary of calibrated predictions
    """
    calibrated = {}

    for row_id, pred in predictions.items():
        # Apply calibration
        new_pred = pred * scale + shift

        # Clip to valid range
        new_pred = max(min(new_pred, 1.0 - 1e-15), 1e-15)

        calibrated[row_id] = new_pred

    logger.info(f"Calibrated {len(calibrated)} predictions (shift={shift}, scale={scale})")
    return calibrated


def compute_ensemble_diversity(
    predictions_list: List[Dict[str, float]]
) -> Dict[str, float]:
    """
    Compute diversity metrics for ensemble

    Args:
        predictions_list: List of prediction dictionaries

    Returns:
        Dictionary with diversity metrics
    """
    if len(predictions_list) < 2:
        return {'diversity': 0.0}

    # Get common IDs
    common_ids = set(predictions_list[0].keys())
    for preds in predictions_list[1:]:
        common_ids = common_ids.intersection(set(preds.keys()))

    # Compute pairwise correlations
    correlations = []
    n_models = len(predictions_list)

    for i in range(n_models):
        for j in range(i + 1, n_models):
            # Get predictions for common IDs
            preds_i = [predictions_list[i][id_] for id_ in common_ids]
            preds_j = [predictions_list[j][id_] for id_ in common_ids]

            # Compute correlation
            mean_i = arithmetic_mean(preds_i)
            mean_j = arithmetic_mean(preds_j)

            cov = sum((pi - mean_i) * (pj - mean_j)
                      for pi, pj in zip(preds_i, preds_j)) / len(preds_i)

            std_i = math.sqrt(sum((pi - mean_i) ** 2 for pi in preds_i) / len(preds_i))
            std_j = math.sqrt(sum((pj - mean_j) ** 2 for pj in preds_j) / len(preds_j))

            if std_i > 0 and std_j > 0:
                corr = cov / (std_i * std_j)
                correlations.append(corr)

    avg_correlation = arithmetic_mean(correlations) if correlations else 0.0
    diversity = 1.0 - avg_correlation

    return {
        'diversity': diversity,
        'avg_correlation': avg_correlation,
        'pairwise_correlations': correlations
    }


if __name__ == '__main__':
    # Example usage
    from utils.logging_utils import setup_logger

    setup_logger('ensemble', log_file='logs/ensemble.log')

    # Test blending methods
    values = [0.15, 0.18, 0.16, 0.17, 0.14]

    print(f"Values: {values}")
    print(f"Arithmetic mean: {arithmetic_mean(values):.6f}")
    print(f"Harmonic mean: {harmonic_mean(values):.6f}")
    print(f"Geometric mean: {geometric_mean(values):.6f}")

    # Test weighted average
    weights = [0.3, 0.25, 0.2, 0.15, 0.1]
    print(f"Weighted average: {weighted_average(values, weights):.6f}")
