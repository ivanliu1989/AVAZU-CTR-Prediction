"""
Logging utilities for AVAZU CTR Prediction
===========================================
Provides standardized logging across all modules.

Usage:
    from utils.logging_utils import setup_logger, get_logger

    # In main script
    setup_logger('my_script', log_file='logs/training.log')

    # In any module
    logger = get_logger(__name__)
    logger.info("Training started")
    logger.error("An error occurred", exc_info=True)
"""
import logging
import os
from typing import Optional
from datetime import datetime


def setup_logger(
    name: str,
    log_file: Optional[str] = None,
    level: int = logging.INFO,
    format_string: Optional[str] = None
) -> logging.Logger:
    """
    Setup a logger with console and optionally file output

    Args:
        name: Logger name
        log_file: Optional path to log file
        level: Logging level (default: INFO)
        format_string: Custom format string

    Returns:
        Configured logger instance
    """
    if format_string is None:
        format_string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Remove existing handlers to avoid duplicates
    logger.handlers = []

    formatter = logging.Formatter(format_string)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler (if specified)
    if log_file:
        # Create log directory if it doesn't exist
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get or create a logger with standard configuration

    Args:
        name: Logger name (typically __name__)

    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)

    # If logger has no handlers, set up default configuration
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def create_timestamped_log_file(base_name: str, log_dir: str = 'logs') -> str:
    """
    Create a timestamped log file path

    Args:
        base_name: Base name for the log file (e.g., 'training')
        log_dir: Directory for log files (default: 'logs')

    Returns:
        Full path to timestamped log file
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{base_name}_{timestamp}.log"
    return os.path.join(log_dir, filename)


class LogProgress:
    """
    Context manager for logging progress of long-running operations

    Usage:
        with LogProgress(logger, "Training model", total=1000) as progress:
            for i in range(1000):
                # ... do work ...
                progress.update(i)
    """
    def __init__(
        self,
        logger: logging.Logger,
        task_name: str,
        total: Optional[int] = None,
        log_interval: int = 100000
    ):
        self.logger = logger
        self.task_name = task_name
        self.total = total
        self.log_interval = log_interval
        self.start_time = None
        self.last_logged = 0

    def __enter__(self):
        self.start_time = datetime.now()
        self.logger.info(f"Started: {self.task_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = datetime.now() - self.start_time
        if exc_type is None:
            self.logger.info(
                f"Completed: {self.task_name} (elapsed: {elapsed})"
            )
        else:
            self.logger.error(
                f"Failed: {self.task_name} (elapsed: {elapsed})",
                exc_info=True
            )
        return False

    def update(self, current: int, extra_info: str = ""):
        """
        Update progress and log if interval reached

        Args:
            current: Current iteration number
            extra_info: Additional information to log
        """
        if current - self.last_logged >= self.log_interval:
            elapsed = datetime.now() - self.start_time

            if self.total:
                pct = (current / self.total) * 100
                msg = f"{self.task_name}: {current:,}/{self.total:,} ({pct:.1f}%)"
            else:
                msg = f"{self.task_name}: {current:,} processed"

            if extra_info:
                msg += f" - {extra_info}"

            msg += f" (elapsed: {elapsed})"
            self.logger.info(msg)
            self.last_logged = current


if __name__ == '__main__':
    # Example usage
    logger = setup_logger(
        'test_logger',
        log_file='logs/test.log',
        level=logging.DEBUG
    )

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")

    # Test progress logger
    with LogProgress(logger, "Test task", total=1000, log_interval=250) as progress:
        for i in range(1000):
            progress.update(i, f"Loss: {0.5 - i/2000:.4f}")
