"""Measures of central tendency: mean, median, and mode.

Covers the "Measures of Central Tendency" section of
https://realpython.com/python-statistics/
"""

import math
import statistics

import numpy as np
import pandas as pd
import scipy.stats

from datasets import one_dimensional


def mean():
    """Calculate the arithmetic mean with pure Python, NumPy, and pandas."""
    x, x_with_nan, y, y_with_nan, z, z_with_nan = one_dimensional()

    print("Pure Python:")
    print(f"  sum(x) / len(x)          = {sum(x) / len(x)}")
    print(f"  statistics.mean(x)       = {statistics.mean(x)}")
    print(f"  statistics.fmean(x)      = {statistics.fmean(x)}")

    # A single nan in the data makes the result nan.
    print(f"  statistics.mean(x_with_nan)  = {statistics.mean(x_with_nan)}")

    print("NumPy:")
    print(f"  np.mean(y)               = {np.mean(y)}")
    print(f"  y.mean()                 = {y.mean()}")
    print(f"  np.mean(y_with_nan)      = {np.mean(y_with_nan)}")
    # Use the nan-safe variant to ignore missing values instead.
    print(f"  np.nanmean(y_with_nan)   = {np.nanmean(y_with_nan)}")

    print("pandas:")
    # pandas skips nan values by default.
    print(f"  z.mean()                 = {z.mean()}")
    print(f"  z_with_nan.mean()        = {z_with_nan.mean()}")


def weighted_mean():
    """Calculate the weighted mean, where each item has its own weight."""
    x = [8.0, 1, 2.5, 4, 28.0]
    w = [0.1, 0.2, 0.3, 0.25, 0.15]

    wmean = sum(w_ * x_ for (x_, w_) in zip(x, w)) / sum(w)
    print(f"Pure Python: {wmean}")

    y, z, w_array = np.array(x), pd.Series(x), np.array(w)
    print(f"np.average(y, weights=w) = {np.average(y, weights=w_array)}")
    print(f"np.average(z, weights=w) = {np.average(z, weights=w_array)}")
    print(f"(w * y).sum() / w.sum()  = {(w_array * y).sum() / w_array.sum()}")


def harmonic_mean():
    """Calculate the harmonic mean, the reciprocal of the mean reciprocal."""
    x, _, y, _, z, _ = one_dimensional()

    hmean = len(x) / sum(1 / item for item in x)
    print(f"Pure Python:                 {hmean}")
    print(f"statistics.harmonic_mean(x): {statistics.harmonic_mean(x)}")
    print(f"scipy.stats.hmean(y):        {scipy.stats.hmean(y)}")
    print(f"scipy.stats.hmean(z):        {scipy.stats.hmean(z)}")

    # A negative value has no harmonic mean.
    try:
        statistics.harmonic_mean([1, 2, -2])
    except statistics.StatisticsError as error:
        print(f"harmonic_mean([1, 2, -2]) raises StatisticsError: {error}")


def geometric_mean():
    """Calculate the geometric mean, the nth root of the product."""
    x, _, y, _, z, _ = one_dimensional()

    gmean = 1
    for item in x:
        gmean *= item
    gmean **= 1 / len(x)

    print(f"Pure Python:                  {gmean}")
    print(f"statistics.geometric_mean(x): {statistics.geometric_mean(x)}")
    print(f"scipy.stats.gmean(y):         {scipy.stats.gmean(y)}")
    print(f"scipy.stats.gmean(z):         {scipy.stats.gmean(z)}")


def median():
    """Find the median, the middle value of the sorted data."""
    x, x_with_nan, y, y_with_nan, z, z_with_nan = one_dimensional()

    n = len(x)
    if n % 2:
        median_ = sorted(x)[round(0.5 * (n - 1))]
    else:
        x_ord, index = sorted(x), round(0.5 * n)
        median_ = 0.5 * (x_ord[index - 1] + x_ord[index])
    print(f"Pure Python:          {median_}")

    print(f"statistics.median(x): {statistics.median(x)}")
    # With an even number of items, the median averages the two middle values.
    print(f"median(x[:-1]):       {statistics.median(x[:-1])}")
    print(f"median_low(x[:-1]):   {statistics.median_low(x[:-1])}")
    print(f"median_high(x[:-1]):  {statistics.median_high(x[:-1])}")

    print(f"np.median(y):         {np.median(y)}")
    print(f"np.nanmedian(y_with_nan): {np.nanmedian(y_with_nan)}")
    print(f"z.median():           {z.median()}")
    print(f"z_with_nan.median():  {z_with_nan.median()}")


def mode():
    """Find the mode, the value that appears most often."""
    u = [2, 3, 2, 8, 12]
    v = [12, 15, 12, 15, 21, 15, 12]

    mode_ = max((u.count(item), item) for item in set(u))[1]
    print(f"Pure Python:            {mode_}")
    print(f"statistics.mode(u):     {statistics.mode(u)}")
    print(f"statistics.multimode(u): {statistics.multimode(u)}")

    # multimode() returns every modal value, mode() only the first.
    print(f"statistics.mode(v):     {statistics.mode(v)}")
    print(f"statistics.multimode(v): {statistics.multimode(v)}")

    u_array, v_array = np.array(u), np.array(v)
    print(f"scipy.stats.mode(u):    {scipy.stats.mode(u_array)}")

    result = scipy.stats.mode(v_array)
    print(f"scipy.stats.mode(v):    {result}")
    print(f"  .mode  = {result.mode}")
    print(f"  .count = {result.count}")

    # pandas returns a Series, so it can report several modal values at once.
    u_series = pd.Series(u)
    v_series = pd.Series(v)
    w_series = pd.Series([2, 2, math.nan])
    print(f"u.mode():\n{u_series.mode()}")
    print(f"v.mode():\n{v_series.mode()}")
    print(f"w.mode():\n{w_series.mode()}")


if __name__ == "__main__":
    for section in (
        mean,
        weighted_mean,
        harmonic_mean,
        geometric_mean,
        median,
        mode,
    ):
        title = section.__name__.replace("_", " ").title()
        print(f"\n{title}\n{'-' * len(title)}")
        section()
