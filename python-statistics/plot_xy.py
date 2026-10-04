"""Draw an x-y plot with its regression line.

Covers the "X-Y Plots" section of https://realpython.com/python-statistics/
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

plt.style.use("ggplot")


def main():
    np.random.seed(seed=0)
    x = np.arange(21)
    y = 5 + 2 * x + 2 * np.random.randn(21)

    slope, intercept, r, *__ = scipy.stats.linregress(x, y)
    line = f"Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}"

    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=0, marker="s", label="Data points")
    ax.plot(x, intercept + slope * x, label=line)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(facecolor="white")
    plt.show()


if __name__ == "__main__":
    main()
