"""Measures of variability: variance, standard deviation, skewness, and more.

Covers the "Measures of Variability" section of
https://realpython.com/python-statistics/
"""

import statistics

import numpy as np
import pandas as pd
import scipy.stats

from datasets import one_dimensional, percentile_data


def variance():
    """Calculate the sample variance, the mean squared deviation."""
    x, x_with_nan, y, y_with_nan, z, z_with_nan = one_dimensional()

    n = len(x)
    mean_ = sum(x) / n
    var_ = sum((item - mean_) ** 2 for item in x) / (n - 1)
    print(f"Pure Python:            {var_}")
    print(f"statistics.variance(x): {statistics.variance(x)}")

    # ddof=1 asks NumPy for the sample variance rather than the population one.
    print(f"np.var(y, ddof=1):      {np.var(y, ddof=1)}")
    print(f"y.var(ddof=1):          {y.var(ddof=1)}")
    print(f"np.nanvar(y_with_nan, ddof=1): {np.nanvar(y_with_nan, ddof=1)}")

    # pandas defaults to ddof=1 and skips nan values.
    print(f"z.var(ddof=1):          {z.var(ddof=1)}")
    print(f"z_with_nan.var(ddof=1): {z_with_nan.var(ddof=1)}")


def standard_deviation():
    """Calculate the standard deviation, the square root of the variance."""
    x, _, y, y_with_nan, z, z_with_nan = one_dimensional()

    var_ = statistics.variance(x)
    print(f"var_ ** 0.5:            {var_**0.5}")
    print(f"statistics.stdev(x):    {statistics.stdev(x)}")

    print(f"np.std(y, ddof=1):      {np.std(y, ddof=1)}")
    print(f"y.std(ddof=1):          {y.std(ddof=1)}")
    print(f"np.nanstd(y_with_nan, ddof=1): {np.nanstd(y_with_nan, ddof=1)}")

    print(f"z.std(ddof=1):          {z.std(ddof=1)}")
    print(f"z_with_nan.std(ddof=1): {z_with_nan.std(ddof=1)}")


def skewness():
    """Measure skewness, how asymmetric the data is around its mean."""
    x, x_with_nan, y, y_with_nan, z, z_with_nan = one_dimensional()

    n = len(x)
    mean_ = sum(x) / n
    var_ = sum((item - mean_) ** 2 for item in x) / (n - 1)
    std_ = var_**0.5
    skew_ = (
        sum((item - mean_) ** 3 for item in x)
        * n
        / ((n - 1) * (n - 2) * std_**3)
    )
    print(f"Pure Python:            {skew_}")

    # bias=False applies the correction for statistical bias.
    print(
        f"scipy.stats.skew(y, bias=False): {scipy.stats.skew(y, bias=False)}"
    )
    print(f"z.skew():               {z.skew()}")
    print(f"z_with_nan.skew():      {z_with_nan.skew()}")


def percentiles():
    """Find percentiles and quantiles, the cut points that divide the data."""
    x, y, y_with_nan = percentile_data()

    print(f"quantiles(x, n=2):      {statistics.quantiles(x, n=2)}")
    print(
        "quantiles(x, n=4, inclusive): "
        f"{statistics.quantiles(x, n=4, method='inclusive')}"
    )

    print(f"np.percentile(y, 5):    {np.percentile(y, 5)}")
    print(f"np.percentile(y, 95):   {np.percentile(y, 95)}")
    print(f"np.percentile(y, [25, 50, 75]): {np.percentile(y, [25, 50, 75])}")
    print(
        "np.nanpercentile(y_with_nan, [25, 50, 75]): "
        f"{np.nanpercentile(y_with_nan, [25, 50, 75])}"
    )

    # quantile() takes fractions between 0 and 1 instead of percentages.
    print(f"np.quantile(y, 0.05):   {np.quantile(y, 0.05)}")
    print(
        f"np.quantile(y, [0.25, 0.5, 0.75]): {np.quantile(y, [0.25, 0.5, 0.75])}"
    )

    z, z_with_nan = pd.Series(y), pd.Series(y_with_nan)
    print(f"z.quantile(0.05):       {z.quantile(0.05)}")
    print(f"z.quantile([0.25, 0.5, 0.75]):\n{z.quantile([0.25, 0.5, 0.75])}")
    print(
        "z_with_nan.quantile([0.25, 0.5, 0.75]):\n"
        f"{z_with_nan.quantile([0.25, 0.5, 0.75])}"
    )


def ranges():
    """Calculate the range and the interquartile range."""
    x, y, y_with_nan = percentile_data()
    z, z_with_nan = pd.Series(y), pd.Series(y_with_nan)

    # np.ptp() returns nan when the data contains nan, whether you pass a
    # NumPy array or a pandas Series.
    print(f"np.ptp(y):              {np.ptp(y)}")
    print(f"np.ptp(z):              {np.ptp(z)}")
    print(f"np.ptp(y_with_nan):     {np.ptp(y_with_nan)}")
    print(f"np.ptp(z_with_nan):     {np.ptp(z_with_nan)}")

    print(f"np.amax(y) - np.amin(y): {np.amax(y) - np.amin(y)}")
    print(
        "np.nanmax(y_with_nan) - np.nanmin(y_with_nan): "
        f"{np.nanmax(y_with_nan) - np.nanmin(y_with_nan)}"
    )
    print(f"z.max() - z.min():      {z.max() - z.min()}")

    # The interquartile range is the distance between the first and third
    # quartiles, which ignores outliers at both ends.
    quartiles = np.quantile(y, [0.25, 0.75])
    print(f"Interquartile range (NumPy):  {quartiles[1] - quartiles[0]}")

    quartiles = z.quantile([0.25, 0.75])
    print(f"Interquartile range (pandas): {quartiles[0.75] - quartiles[0.25]}")


if __name__ == "__main__":
    for section in (
        variance,
        standard_deviation,
        skewness,
        percentiles,
        ranges,
    ):
        title = section.__name__.replace("_", " ").title()
        print(f"\n{title}\n{'-' * len(title)}")
        section()
