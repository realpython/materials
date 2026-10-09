"""Draw a box plot of three random datasets.

Covers the "Box Plots" section of https://realpython.com/python-statistics/
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")


def main():
    np.random.seed(seed=0)
    x = np.random.randn(1000)
    y = np.random.randn(100)
    z = np.random.randn(10)

    fig, ax = plt.subplots()
    ax.boxplot(
        (x, y, z),
        orientation="horizontal",
        showmeans=True,
        meanline=True,
        tick_labels=("x", "y", "z"),
        patch_artist=True,
        medianprops={"linewidth": 2, "color": "purple"},
        meanprops={"linewidth": 2, "color": "red"},
    )
    plt.show()


if __name__ == "__main__":
    main()
