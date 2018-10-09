#!/usr/bin/env python3

"""
Code for "Python Histogram Plotting: NumPy, Matplotlib, Pandas & Seaborn".

https://realpython.com/python-histograms/

To run this script interactively:
$ ipython ./histograms.py -i
or
$ python3 -i ./histograms.py
"""

from collections import Counter
import random
import sys
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns

print(__doc__)


random.seed(1)
np.random.seed(444)
np.set_printoptions(precision=3)
plt.ioff()

# ---------------------------------------------------------------------
# Histograms in Pure Python
# ---------------------------------------------------------------------


def count_elements(seq) -> dict:
    """Tally elements from `seq`."""
    hist = {}
    # Bind method to a variable for faster calls within loop.
    get = hist.get
    for i in seq:
        hist[i] = get(i, 0) + 1
    return hist


a = (0, 1, 1, 1, 2, 3, 7, 7, 23)
counted = count_elements(a)
recounted = Counter(a)
# Both `.items()` are instances of Python builtin `dict_items`.
assert counted.items() == recounted.items(), "Frequency tables unequal."
print("`a`:", a)
print("Manual frequency table of `a`:", counted)
print("With `collections.Counter`:", recounted)
print()


def ascii_histogram(seq) -> None:
    """A horizontal frequency-table/histogram plot."""
    counted = count_elements(seq)
    for k in sorted(counted):
        print("{0:5d} {1}".format(k, "+" * counted[k]))


vals = [1, 3, 4, 6, 8, 9, 10]
# Each number in `vals` will occur between 5 and 15 times.
freq = [random.randint(5, 15) for _ in vals]

data = []
for f, v in zip(freq, vals):
    data.extend([v] * f)
print("ASCII histogram of `data`:")
ascii_histogram(data)
print()


# ---------------------------------------------------------------------
# Histograms Calculations in NumPy
# ---------------------------------------------------------------------

d = np.random.laplace(loc=15, scale=3, size=500)
hist, bin_edges = np.histogram(d)
print("first 5 elements of `d`:", d[:5])
print("hist:", hist)
print("bin_edges:", bin_edges)

bcounts = np.bincount(a)
hist, _ = np.histogram(a, range=(0, max(a)), bins=max(a) + 1)
print(bcounts)
assert np.array_equal(hist, bcounts), "Bincounts unequal."

# Reproducing `collections.Counter`
print(
    "Reproducing `collections.Counter`:",
    dict(zip(np.unique(a), bcounts[bcounts.nonzero()])),
)


# ---------------------------------------------------------------------
# Visualizing Histograms with Matplotlib & Pandas
# ---------------------------------------------------------------------

n, bins, patches = plt.hist(
    x=d, bins="auto", color="#0504aa", alpha=0.7, rwidth=0.85
)
plt.grid(axis="y", alpha=0.75)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("My Very Own Histogram")
plt.text(23, 45, r"$\mu=15, b=3$")
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()


# Generate data on commute times.
size, scale = 1000, 10
commutes = pd.Series(np.random.gamma(scale, size=size) ** 1.5)

commutes.plot.hist(bins=15, rwidth=0.9, color="#607c8e")
plt.title("Commute Times for 1,000 Commuters")
plt.xlabel("Commute Time (min)")
plt.ylabel("Counts")
plt.grid(axis="y", alpha=0.75)
plt.show()

# ---------------------------------------------------------------------
# Plotting a Kernel Density Estimate
# ---------------------------------------------------------------------

# Sample from two different normal distributions.
means = 10, 20
stdevs = 4, 2
dist = pd.DataFrame(
    np.random.normal(loc=means, scale=stdevs, size=(1000, 2)),
    columns=["a", "b"],
)
print(dist.agg(["min", "max", "mean", "std"]).round(decimals=2))

fig, ax = plt.subplots()
dist.plot.kde(ax=ax, grid=True, legend=False, title="Histogram: A vs. B")
dist.plot.hist(density=True, ax=ax)
ax.set_ylabel("Probability")
ax.set_facecolor("#d8dcd6")
ax.grid(axis="y")
plt.show()


# An object representing the "frozen" analytical distribution.
# Defaults to the standard normal distribution, N~(0, 1)
dist = stats.norm()

# Draw random samples from the population you built above.
# This is just a sample, so the mean and std. deviation should
# be close to (1, 0).
samp = dist.rvs(size=1000)

# `ppf()`: percent point function (inverse of cdf — percentiles).
x = np.linspace(start=stats.norm.ppf(0.01), stop=stats.norm.ppf(0.99), num=250)
gkde = stats.gaussian_kde(dataset=samp)

# `gkde.evaluate()` estimates the PDF itself.
fig, ax = plt.subplots()
ax.plot(
    x,
    dist.pdf(x),
    linestyle="solid",
    c="red",
    lw=3,
    alpha=0.8,
    label="Analytical (True) PDF",
)
ax.plot(
    x,
    gkde.evaluate(x),
    linestyle="dashed",
    c="black",
    lw=2,
    label="PDF Estimated via KDE",
)
ax.legend(loc="best", frameon=False)
ax.set_title("Analytical vs. Estimated PDF")
ax.set_ylabel("Probability")
ax.text(-2.0, 0.35, r"$f(x) = \frac{\exp(-x^2/2)}{\sqrt{2*\pi}}$", fontsize=12)
plt.show()

# ---------------------------------------------------------------------
# A Fancy Alternative with Seaborn
# ---------------------------------------------------------------------

sns.set_style("darkgrid")
# Suppress the kwarg warning related to normed/density from Matplotlib.
with warnings.catch_warnings():
    warnings.simplefilter("ignore", category=UserWarning)

    sns.distplot(d)
    plt.title("Seaborn's distplot()")
    plt.show()

    sns.distplot(d, fit=stats.laplace, kde=False)
    plt.title("Histogram with Fitted Laplace Distribution")
    plt.show()


data = np.random.choice(
    np.arange(10), size=10000, p=np.linspace(1, 11, 10) / 60
)
s = pd.Series(data)
print(s.value_counts())
print(s.value_counts(normalize=True).head())

ages = pd.Series(
    [1, 1, 3, 5, 8, 10, 12, 15, 18, 18, 19, 20, 25, 30, 40, 51, 52]
)
bins = (0, 10, 13, 18, 21, np.inf)  # The edges
labels = ("child", "preteen", "teen", "military_age", "adult")
groups, _ = pd.cut(ages, bins=bins, labels=labels, retbins=True)
print(groups.value_counts())
print(pd.concat((ages, groups), axis=1).rename(columns={0: "age", 1: "group"}))

sys.exit()
