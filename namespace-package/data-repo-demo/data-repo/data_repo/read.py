from importlib import resources

import pandas as pd


def data(name, package=__package__):
    """Get data file."""
    data_path = path(name, package)
    file_type = data_path.suffix.lstrip(".")
    return readers[file_type](data_path)


def path(name, package=__package__):
    """Find the path to a data file."""
    for resource in resources.files(package).iterdir():
        if resource.stem == name:
            return resource

    raise FileNotFoundError(f"{name} not found in {package}")


def csv(data_path):
    """Read CSV file from a path."""
    return pd.read_csv(data_path)


def json(data_path):
    """Read JSON file from a path."""
    return pd.read_json(data_path)


readers = {"csv": csv, "json": json}
