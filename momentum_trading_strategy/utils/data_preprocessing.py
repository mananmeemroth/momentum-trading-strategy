import pandas as pd

def load_data(file_path):
    """Load CSV data for stock price"""
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    return df

def merge_datasets(files):
    """Merge data from multiple stock files into a single DataFrame"""
    dfs = []
    for file in files:
        dfs.append(load_data(file))
    data = pd.concat(dfs, axis=1, keys=[file.split('.')[0] for file in files])
    return data
