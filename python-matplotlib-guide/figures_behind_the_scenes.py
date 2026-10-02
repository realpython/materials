"""Inspect the Figures that matplotlib keeps around in memory.

Covers the "The 'Figures' Behind The Scenes" section of
https://realpython.com/python-matplotlib-guide/

The id() values below are memory addresses, so your numbers will differ
from the ones printed in the tutorial. Only the comparisons match.
"""

import matplotlib.pyplot as plt


def get_all_figures():
    return [plt.figure(i) for i in plt.get_fignums()]


def main():
    fig1, ax1 = plt.subplots()

    print(id(fig1))
    print(id(plt.gcf()))  # `fig1` is the current figure.

    fig2, ax2 = plt.subplots()
    print(id(fig2) == id(plt.gcf()))  # The current figure is now `fig2`.

    # Both figures are still hanging around in memory, each with a
    # corresponding ID number (1-indexed, in MATLAB style).
    print(plt.get_fignums())
    print(get_all_figures())

    # Close each figure after use to avoid a MemoryError.
    plt.close("all")
    print(get_all_figures())


if __name__ == "__main__":
    main()
