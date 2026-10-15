"""Summarize a whole dataset in a single call.

Covers the "Summary of Descriptive Statistics" section of
https://realpython.com/python-statistics/
"""

import pandas as pd
import scipy.stats

from datasets import percentile_data


def scipy_describe():
    """Summarize an array with scipy.stats.describe()."""
    _, y, _ = percentile_data()

    result = scipy.stats.describe(y, ddof=1, bias=False)
    print(result)

    # Every field is also available as an attribute.
    print(f"  nobs      = {result.nobs}")
    print(f"  min       = {result.minmax[0]}")
    print(f"  max       = {result.minmax[1]}")
    print(f"  mean      = {result.mean}")
    print(f"  variance  = {result.variance}")
    print(f"  skewness  = {result.skewness}")
    print(f"  kurtosis  = {result.kurtosis}")


def pandas_describe():
    """Summarize a Series with .describe()."""
    _, y, _ = percentile_data()
    z = pd.Series(y)

    result = z.describe()
    print(result)

    # The result is itself a Series, so you index it by label.
    for label in ("mean", "std", "min", "max", "25%", "50%", "75%"):
        print(f"  {label:<4} = {result[label]}")


if __name__ == "__main__":
    for section in (scipy_describe, pandas_describe):
        title = section.__name__.replace("_", " ").title()
        print(f"\n{title}\n{'-' * len(title)}")
        section()
