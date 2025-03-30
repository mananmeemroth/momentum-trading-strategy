import pandas as pd
import numpy as np

def calculate_sma(data, window=20):
    """Calculate Simple Moving Average (SMA)"""
    return data['Close'].rolling(window=window).mean()

def calculate_rsi(data, window=14):
    """Calculate the Relative Strength Index (RSI)"""
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def calculate_roc(data, window=10):
    """Calculate Rate of Change (ROC)"""
    return data['Close'].pct_change(periods=window) * 100
