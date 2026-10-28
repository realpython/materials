"""Create Figures and Axes with plt.subplots().

Covers the "Understanding plt.subplots() Notation" section of
https://realpython.com/python-matplotlib-guide/
"""

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(444)


def single_axes():
    """Show that the default call returns one Figure and one Axes."""
    fig, ax = plt.subplots()
    print(type(ax))


def stacked_area():
    """Draw a stacked area graph of three random time series."""
    rng = np.arange(50)
    rnd = np.random.randint(0, 10, size=(3, rng.size))
    yrs = 1950 + rng

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.stackplot(yrs, rng + rnd, labels=["Eastasia", "Eurasia", "Oceania"])
    ax.set_title("Combined debt growth over time")
    ax.legend(loc="upper left")
    ax.set_ylabel("Total debt")
    ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
    fig.tight_layout()
    plt.show()


def two_subplots():
    """Put two correlated arrays into a 1x2 grid of Axes."""
    x = np.random.randint(low=1, high=11, size=50)
    y = x + np.random.randint(1, 5, size=x.size)
    data = np.column_stack((x, y))

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

    ax1.scatter(x=x, y=y, marker="o", c="r", edgecolor="b")
    ax1.set_title("Scatter: $x$ versus $y$")
    ax1.set_xlabel("$x$")
    ax1.set_ylabel("$y$")

    ax2.hist(data, bins=np.arange(data.min(), data.max()), label=("x", "y"))
    ax2.legend(loc=(0.65, 0.8))
    ax2.set_title("Frequencies of $x$ and $y$")
    ax2.yaxis.tick_right()

    # Multiple Axes can "belong to" a given Figure.
    print((fig.axes[0] is ax1, fig.axes[1] is ax2))
    plt.show()


def grid_of_axes():
    """Show that a 2x2 call returns a NumPy array of Axes."""
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
    print(type(ax))
    print(repr(ax))
    print(ax.shape)

    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
    ax1, ax2, ax3, ax4 = ax.flatten()  # flatten a 2d NumPy array to 1d
    print(ax1, ax2, ax3, ax4)


if __name__ == "__main__":
    for section in (single_axes, stacked_area, two_subplots, grid_of_axes):
        title = section.__name__.replace("_", " ").title()
        print(f"\n{title}\n{'-' * len(title)}")
        section()
