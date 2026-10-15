"""Measures of correlation between pairs of data.

Covers the "Measures of Correlation Between Pairs of Data" section of
https://realpython.com/python-statistics/
"""

import numpy as np
import scipy.stats

from datasets import correlation_data


def covariance():
    """Calculate the covariance, which measures joint variability."""
    x, y, x_, y_, x__, y__ = correlation_data()

    n = len(x)
    mean_x, mean_y = sum(x) / n, sum(y) / n
    cov_xy = sum((x[k] - mean_x) * (y[k] - mean_y) for k in range(n)) / (n - 1)
    print(f"Pure Python:            {cov_xy}")

    # np.cov() returns the covariance matrix, not a single number. Its
    # diagonal holds the variances and its off-diagonal the covariance.
    cov_matrix = np.cov(x_, y_)
    print(f"np.cov(x_, y_) =\n{cov_matrix}")
    print(f"  variance of x: {x_.var(ddof=1)}")
    print(f"  variance of y: {y_.var(ddof=1)}")
    print(f"  covariance:    {cov_matrix[0, 1]}")

    print(f"x__.cov(y__):           {x__.cov(y__)}")


def correlation_coefficient():
    """Calculate Pearson's r, the normalized measure of correlation."""
    x, y, x_, y_, x__, y__ = correlation_data()

    n = len(x)
    mean_x, mean_y = sum(x) / n, sum(y) / n
    var_x = sum((item - mean_x) ** 2 for item in x) / (n - 1)
    var_y = sum((item - mean_y) ** 2 for item in y) / (n - 1)
    std_x, std_y = var_x**0.5, var_y**0.5
    cov_xy = sum((x[k] - mean_x) * (y[k] - mean_y) for k in range(n)) / (n - 1)
    print(f"Pure Python:            {cov_xy / (std_x * std_y)}")

    # pearsonr() returns the coefficient and the p-value together.
    r, p = scipy.stats.pearsonr(x_, y_)
    print(f"scipy.stats.pearsonr(): r={r}, p={p}")

    corr_matrix = np.corrcoef(x_, y_)
    print(f"np.corrcoef(x_, y_) =\n{corr_matrix}")
    print(f"  r = {corr_matrix[0, 1]}")

    print(f"x__.corr(y__):          {x__.corr(y__)}")


def linear_regression():
    """Fit a regression line, which also reports the correlation."""
    *_, x_, y_, __, ___ = correlation_data()

    result = scipy.stats.linregress(x_, y_)
    print(result)
    print(f"  slope     = {result.slope}")
    print(f"  intercept = {result.intercept}")
    print(f"  rvalue    = {result.rvalue}")


if __name__ == "__main__":
    for section in (covariance, correlation_coefficient, linear_regression):
        title = section.__name__.replace("_", " ").title()
        print(f"\n{title}\n{'-' * len(title)}")
        section()
