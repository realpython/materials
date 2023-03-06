import pandas as pd


def read(data_path):
    """Read CSV file from a path."""
    return pd.read_csv(data_path)
