import numpy as np

def calculate_returns(data):
    """Calculate daily returns"""
    data['Returns'] = data['Close'].pct_change()
    return data

def calculate_sharpe_ratio(data, risk_free_rate=0.01):
    """Calculate Sharpe ratio"""
    excess_returns = data['Returns'] - risk_free_rate / 252
    return np.sqrt(252) * excess_returns.mean() / excess_returns.std()

def calculate_drawdown(data):
    """Calculate drawdown"""
    data['Cumulative Returns'] = (1 + data['Returns']).cumprod()
    data['Max'] = data['Cumulative Returns'].cummax()
    data['Drawdown'] = (data['Cumulative Returns'] - data['Max']) / data['Max']
    return data
