"""Lay out uneven subplots with gridspec and subplot2grid().

Covers the gridspec examples in the "Understanding plt.subplots()
Notation" section of https://realpython.com/python-matplotlib-guide/

The California housing data is downloaded from figshare at runtime, so
this script needs an internet connection.
"""

from io import BytesIO
import tarfile
from urllib.request import urlopen

import matplotlib.pyplot as plt
import numpy as np


def load_housing():
    """Pull the macroeconomic California housing data."""
    url = "https://ndownloader.figshare.com/files/5976036"
    b = BytesIO(urlopen(url).read())
    fpath = "CaliforniaHousing/cal_housing.data"

    with tarfile.open(mode="r", fileobj=b) as archive:
        housing = np.loadtxt(archive.extractfile(fpath), delimiter=",")

    return housing


def add_titlebox(ax, text):
    """Place a text box inside a plot as an "in-plot title"."""
    ax.text(
        0.55,
        0.8,
        text,
        horizontalalignment="center",
        transform=ax.transAxes,
        bbox=dict(facecolor="white", alpha=0.6),
        fontsize=12.5,
    )
    return ax


def main():
    housing = load_housing()

    # The "response" variable y is an area's average home value. pop
    # and age are the area's population and average house age.
    y = housing[:, -1]
    pop, age = housing[:, [4, 7]].T

    # A 3x2 grid where ax1 spans two columns and two rows.
    gridsize = (3, 2)
    # The tutorial binds this Figure to `fig`, but never uses it.
    plt.figure(figsize=(12, 8))
    ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
    ax2 = plt.subplot2grid(gridsize, (2, 0))
    ax3 = plt.subplot2grid(gridsize, (2, 1))

    ax1.set_title(
        "Home value as a function of home age & area population",
        fontsize=14,
    )
    sctr = ax1.scatter(x=age, y=pop, c=y, cmap="RdYlGn")
    plt.colorbar(sctr, ax=ax1, format="$%d")
    ax1.set_yscale("log")
    ax2.hist(age, bins="auto")
    ax3.hist(pop, bins="auto", log=True)

    add_titlebox(ax2, "Histogram: home age")
    add_titlebox(ax3, "Histogram: area population (log scl.)")
    plt.show()


if __name__ == "__main__":
    main()
