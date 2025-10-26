"""
Machine Learning Models for AVAZU CTR Prediction
"""
from .ftrl import FTRLProximal, train_ftrl, logloss

__all__ = ['FTRLProximal', 'train_ftrl', 'logloss']
