def backtest_strategy(data, indicator, threshold=70):
    """Simple momentum strategy using RSI"""
    positions = []
    for i in range(1, len(data)):
        if indicator[i-1] < threshold and indicator[i] >= threshold:
            positions.append('Buy')
        elif indicator[i-1] > threshold and indicator[i] <= threshold:
            positions.append('Sell')
        else:
            positions.append('Hold')
    
    data['Position'] = ['Hold'] + positions
    return data
