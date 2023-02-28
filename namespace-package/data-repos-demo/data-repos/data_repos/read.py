from importlib import resources

import pandas as pd


def data(name):
    """Get a data file."""
    data_path = path(name)
    file_type = data_path.suffix.lstrip(".")
    return readers[file_type](data_path)


def path(name):
    """Find the path to a data file."""
    for resource in resources.files(__package__).iterdir():
        if resource.stem == name:
            return resource
    raise FileNotFoundError(f"{name} not found in {__package__}")


def csv(data_path):
    """Read a CSV file from a path."""
    return pd.read_csv(data_path)


def json(data_path):
    """Read a JSON file from a path."""
    return pd.read_json(data_path)


readers = {"csv": csv, "json": json}
