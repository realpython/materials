"""Example datasets used throughout the tutorial.

Each function returns the data for one section of
https://realpython.com/python-statistics/ so that the other scripts in this
folder can stay short and focused on the statistics themselves.
"""

import math

import numpy as np
import pandas as pd


def one_dimensional():
    """Return the small 1D dataset used for central tendency and variability.

    Returns a plain list, a NumPy array, and a pandas Series, each in a
    version with and without a ``nan`` value.
    """
    x = [8.0, 1, 2.5, 4, 28.0]
    x_with_nan = [8.0, 1, 2.5, math.nan, 4, 28.0]

    y, y_with_nan = np.array(x), np.array(x_with_nan)
    z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)

    return x, x_with_nan, y, y_with_nan, z, z_with_nan


def percentile_data():
    """Return the nine-value dataset used in the percentiles section."""
    x = [-5.0, -1.1, 0.1, 2.0, 8.0, 12.8, 21.0, 25.8, 41.0]
    y = np.array(x)
    y_with_nan = np.insert(y, 2, np.nan)

    return x, y, y_with_nan


def correlation_data():
    """Return the paired dataset used for covariance and correlation."""
    x = list(range(-10, 11))
    y = [0, 2, 2, 2, 2, 3, 3, 6, 7, 4, 7, 6, 6, 9, 4, 5, 5, 10, 11, 12, 14]

    x_, y_ = np.array(x), np.array(y)
    x__, y__ = pd.Series(x_), pd.Series(y_)

    return x, y, x_, y_, x__, y__


def two_dimensional():
    """Return the 5x3 array used in the sections on axes and DataFrames."""
    return np.array(
        [
            [1, 1, 1],
            [2, 3, 1],
            [4, 9, 2],
            [8, 27, 4],
            [16, 1, 1],
        ]
    )


if __name__ == "__main__":
    x, x_with_nan, y, y_with_nan, z, z_with_nan = one_dimensional()
    print(f"{x = }")
    print(f"{x_with_nan = }")
    print(f"y =\n{y}\n")
    print(f"z =\n{z}\n")
    print(f"2D array a =\n{two_dimensional()}")
