"""Draw a bar chart with error bars.

Covers the "Bar Charts" section of https://realpython.com/python-statistics/
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")


def main():
    np.random.seed(seed=0)
    x = np.arange(21)
    y = np.random.randint(21, size=21)
    # Error bar sizes must be non-negative, so take the absolute values.
    err = np.abs(np.random.randn(21))

    fig, ax = plt.subplots()
    ax.bar(x, y, yerr=err)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    plt.show()


if __name__ == "__main__":
    main()
