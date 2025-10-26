"""
Data Preprocessing Utilities for AVAZU CTR Prediction
======================================================
Reusable preprocessing functions for feature engineering and data cleaning.

Usage:
    from utils.preprocessing import handle_null_values, extract_temporal_features

    df = handle_null_values(df, config.preprocessing.null_values)
    df = extract_temporal_features(df)
"""
import csv
import logging
from typing import List, Dict, Tuple, Iterator
from datetime import datetime
from collections import Counter

logger = logging.getLogger(__name__)


def handle_null_values(
    row: Dict[str, str],
    null_values: List[str]
) -> Dict[str, str]:
    """
    Replace null value indicators with empty strings

    Args:
        row: Dictionary of feature values
        null_values: List of strings indicating null values

    Returns:
        Dictionary with null values replaced
    """
    for key, value in row.items():
        if value in null_values:
            row[key] = ''
    return row


def extract_temporal_features(hour_str: str) -> Dict[str, int]:
    """
    Extract temporal features from YYMMDDHH format

    Args:
        hour_str: Hour in YYMMDDHH format (e.g., '14102100')

    Returns:
        Dictionary with extracted features:
            - hour: Hour of day (0-23)
            - day: Day of month (1-31)
            - day_of_week: Day of week (0=Monday, 6=Sunday)
            - is_weekend: 1 if weekend, 0 otherwise
            - is_halloween: 1 if Oct 31, 0 otherwise
    """
    try:
        # Parse YYMMDDHH
        year = int('20' + hour_str[:2])
        month = int(hour_str[2:4])
        day = int(hour_str[4:6])
        hour = int(hour_str[6:])

        # Create date object
        date = datetime(year, month, day, hour)

        # Extract features
        features = {
            'hour': hour,
            'day': day,
            'day_of_week': date.weekday(),  # 0=Monday, 6=Sunday
            'is_weekend': 1 if date.weekday() >= 5 else 0,
            'is_halloween': 1 if (month == 10 and day == 31) else 0,
        }

        return features

    except (ValueError, IndexError) as e:
        logger.warning(f"Error parsing hour string '{hour_str}': {e}")
        return {
            'hour': 0,
            'day': 0,
            'day_of_week': 0,
            'is_weekend': 0,
            'is_halloween': 0,
        }


def split_by_category(
    input_file: str,
    output_site: str,
    output_app: str,
    split_column: str = 'app_id'
) -> Tuple[int, int]:
    """
    Split data into site and app categories

    Args:
        input_file: Path to input CSV file
        output_site: Path to output site CSV
        output_app: Path to output app CSV
        split_column: Column to use for splitting (default: 'app_id')

    Returns:
        Tuple of (site_count, app_count)
    """
    site_count = 0
    app_count = 0

    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames

            with open(output_site, 'w', newline='') as site_file, \
                 open(output_app, 'w', newline='') as app_file:

                site_writer = csv.DictWriter(site_file, fieldnames=fieldnames)
                app_writer = csv.DictWriter(app_file, fieldnames=fieldnames)

                site_writer.writeheader()
                app_writer.writeheader()

                for row in reader:
                    if row[split_column] == '' or row[split_column] in ['d41d8cd9', 'ecad2386']:
                        site_writer.writerow(row)
                        site_count += 1
                    else:
                        app_writer.writerow(row)
                        app_count += 1

        logger.info(f"Split complete: {site_count} site rows, {app_count} app rows")
        return site_count, app_count

    except FileNotFoundError:
        logger.error(f"Input file not found: {input_file}")
        raise
    except Exception as e:
        logger.error(f"Error splitting file: {e}")
        raise


def compute_ctr_smoothing(
    data: Iterator[Dict[str, str]],
    feature_cols: List[str],
    target_col: str = 'click',
    alpha: float = 10.0
) -> Dict[str, float]:
    """
    Compute Laplace-smoothed CTR for categorical features

    Args:
        data: Iterator of data rows
        feature_cols: List of feature column names
        target_col: Name of target column (default: 'click')
        alpha: Laplace smoothing parameter (default: 10.0)

    Returns:
        Dictionary mapping feature_value to smoothed CTR
    """
    feature_stats = {}

    for row in data:
        for col in feature_cols:
            key = f"{col}_{row[col]}"

            if key not in feature_stats:
                feature_stats[key] = {'clicks': 0, 'impressions': 0}

            feature_stats[key]['impressions'] += 1
            if row.get(target_col) == '1':
                feature_stats[key]['clicks'] += 1

    # Compute smoothed CTR
    ctr_map = {}
    for key, stats in feature_stats.items():
        smoothed_ctr = (stats['clicks'] + alpha) / (stats['impressions'] + alpha * 2)
        ctr_map[key] = smoothed_ctr

    logger.info(f"Computed CTR for {len(ctr_map)} feature values")
    return ctr_map


def filter_rare_features(
    data: Iterator[Dict[str, str]],
    feature_cols: List[str],
    min_count: int = 5
) -> Dict[str, set]:
    """
    Identify rare features to be filtered

    Args:
        data: Iterator of data rows
        feature_cols: List of feature column names
        min_count: Minimum occurrence count (default: 5)

    Returns:
        Dictionary mapping column names to set of rare values
    """
    feature_counts = {col: Counter() for col in feature_cols}

    # Count occurrences
    for row in data:
        for col in feature_cols:
            if col in row:
                feature_counts[col][row[col]] += 1

    # Identify rare values
    rare_values = {}
    for col, counts in feature_counts.items():
        rare = {value for value, count in counts.items() if count < min_count}
        rare_values[col] = rare
        logger.info(f"Column '{col}': {len(rare)} rare values (< {min_count} occurrences)")

    return rare_values


def one_hot_encode(
    value: str,
    feature_name: str
) -> List[str]:
    """
    One-hot encode a feature value

    Args:
        value: Feature value
        feature_name: Name of the feature
        cardinality_threshold: Max distinct values for one-hot encoding

    Returns:
        List of one-hot encoded feature strings
    """
    return [f"{feature_name}_{value}"]


def hash_feature(
    key: str,
    value: str,
    D: int = 2 ** 28
) -> int:
    """
    Hash a feature using the hash trick

    Args:
        key: Feature name
        value: Feature value
        D: Hash space dimension

    Returns:
        Hashed feature index
    """
    feature_str = f"{key}_{value}"
    return hash(feature_str) % D


def generate_feature_interactions(
    features: List[int],
    D: int = 2 ** 28
) -> List[int]:
    """
    Generate 2-way feature interactions

    Args:
        features: List of feature indices
        D: Hash space dimension

    Returns:
        List of interaction feature indices
    """
    interactions = []
    features_sorted = sorted(features)
    n = len(features_sorted)

    for i in range(n):
        for j in range(i + 1, n):
            interaction_key = f"{features_sorted[i]}_{features_sorted[j]}"
            interaction_idx = hash(interaction_key) % D
            interactions.append(interaction_idx)

    return interactions


def stream_csv_chunks(
    file_path: str,
    chunk_size: int = 100000
) -> Iterator[List[Dict[str, str]]]:
    """
    Stream CSV file in chunks

    Args:
        file_path: Path to CSV file
        chunk_size: Number of rows per chunk

    Yields:
        List of row dictionaries (chunk)
    """
    chunk = []

    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                chunk.append(row)

                if len(chunk) >= chunk_size:
                    yield chunk
                    chunk = []

            # Yield remaining rows
            if chunk:
                yield chunk

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logger.error(f"Error streaming file: {e}")
        raise


def validate_data_schema(
    row: Dict[str, str],
    required_columns: List[str]
) -> bool:
    """
    Validate that a data row has all required columns

    Args:
        row: Data row dictionary
        required_columns: List of required column names

    Returns:
        True if valid, False otherwise
    """
    missing = [col for col in required_columns if col not in row]

    if missing:
        logger.warning(f"Missing columns: {missing}")
        return False

    return True


if __name__ == '__main__':
    # Example usage
    from utils.logging_utils import setup_logger

    setup_logger('preprocessing', log_file='logs/preprocessing.log')

    # Test temporal features
    features = extract_temporal_features('14103100')
    print("Temporal features:", features)

    # Test null handling
    row = {'id': 'test', 'site_id': 'd41d8cd9', 'app_id': '12345'}
    cleaned = handle_null_values(row, ['d41d8cd9'])
    print("Cleaned row:", cleaned)
