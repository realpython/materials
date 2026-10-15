"""Statistics over 2D data, and what the axis argument does.

Covers the "Working With 2D Data" section of
https://realpython.com/python-statistics/
"""

import numpy as np
import scipy.stats

from datasets import two_dimensional


def whole_array():
    """Apply statistics to every value in the array at once."""
    a = two_dimensional()
    print(f"a =\n{a}")

    print(f"np.mean(a):             {np.mean(a)}")
    print(f"a.mean():               {a.mean()}")
    print(f"np.median(a):           {np.median(a)}")
    print(f"a.var(ddof=1):          {a.var(ddof=1)}")


def along_axes():
    """Apply statistics column by column (axis=0) or row by row (axis=1)."""
    a = two_dimensional()

    # axis=0 collapses the rows, leaving one result per column.
    print(f"np.mean(a, axis=0):     {np.mean(a, axis=0)}")
    print(f"np.median(a, axis=0):   {np.median(a, axis=0)}")
    print(f"a.var(axis=0, ddof=1):  {a.var(axis=0, ddof=1)}")

    # axis=1 collapses the columns, leaving one result per row.
    print(f"np.mean(a, axis=1):     {np.mean(a, axis=1)}")
    print(f"np.median(a, axis=1):   {np.median(a, axis=1)}")
    print(f"a.var(axis=1, ddof=1):  {a.var(axis=1, ddof=1)}")

    # SciPy functions take the same argument, and default to axis=0.
    print(f"scipy.stats.gmean(a):   {scipy.stats.gmean(a)}")
    print(f"gmean(a, axis=1):       {scipy.stats.gmean(a, axis=1)}")
    # axis=None flattens the array first.
    print(f"gmean(a, axis=None):    {scipy.stats.gmean(a, axis=None)}")


def describe_by_axis():
    """Summarize a 2D array, flattened and along each axis."""
    a = two_dimensional()

    print("axis=None (the whole array):")
    print(f"  {scipy.stats.describe(a, axis=None, ddof=1, bias=False)}")

    print("axis=0 (per column, the default):")
    print(f"  {scipy.stats.describe(a, ddof=1, bias=False)}")

    print("axis=1 (per row):")
    result = scipy.stats.describe(a, axis=1, ddof=1, bias=False)
    print(f"  {result}")
    print(f"  .mean = {result.mean}")


if __name__ == "__main__":
    for section in (whole_array, along_axes, describe_by_axis):
        title = section.__name__.replace("_", " ").title()
        print(f"\n{title}\n{'-' * len(title)}")
        section()
