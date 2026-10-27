"""Statistics with pandas DataFrame objects.

Covers the "DataFrames" section of https://realpython.com/python-statistics/
"""

import pandas as pd

from datasets import two_dimensional


def build_dataframe():
    """Return the labeled DataFrame used throughout this script."""
    row_names = ["first", "second", "third", "fourth", "fifth"]
    col_names = ["A", "B", "C"]
    return pd.DataFrame(two_dimensional(), index=row_names, columns=col_names)


def by_column_and_row():
    """Calculate statistics across columns and across rows."""
    df = build_dataframe()
    print(f"df =\n{df}\n")

    # DataFrame methods default to working column by column.
    print(f"df.mean():\n{df.mean()}\n")
    print(f"df.var():\n{df.var()}\n")

    # Pass axis=1 to work row by row instead.
    print(f"df.mean(axis=1):\n{df.mean(axis=1)}\n")
    print(f"df.var(axis=1):\n{df.var(axis=1)}")


def single_column():
    """Pull one column out as a Series and work with it directly."""
    df = build_dataframe()

    print(f"df['A']:\n{df['A']}\n")
    print(f"df['A'].mean(): {df['A'].mean()}")
    print(f"df['A'].var():  {df['A'].var()}")


def to_numpy():
    """Drop the labels and get back a plain NumPy array."""
    df = build_dataframe()

    print(f"df.values:\n{df.values}\n")
    print(f"df.to_numpy():\n{df.to_numpy()}")


def describe():
    """Summarize every column at once."""
    df = build_dataframe()

    print(f"df.describe():\n{df.describe()}\n")

    # The summary is a DataFrame too, so .at[] reaches a single value.
    print(f"df.describe().at['mean', 'A']: {df.describe().at['mean', 'A']}")
    print(f"df.describe().at['50%', 'B']:  {df.describe().at['50%', 'B']}")


if __name__ == "__main__":
    for section in (by_column_and_row, single_column, to_numpy, describe):
        title = section.__name__.replace("_", " ").title()
        print(f"\n{title}\n{'-' * len(title)}")
        section()
