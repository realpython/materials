import pandas as pd


def read(data_path):
    """Read JSON file from a path."""
    return pd.read_json(data_path)
