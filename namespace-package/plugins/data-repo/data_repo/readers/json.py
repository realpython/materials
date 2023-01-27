import pandas as pd


def json(data_path):
    """Read JSON file from a path."""
    return pd.read_json(data_path)
