"""Draw heatmaps of the covariance and correlation matrices.

Covers the "Heatmaps" section of https://realpython.com/python-statistics/
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")


def draw_heatmap(matrix):
    """Draw one 2x2 matrix as a heatmap with its values written on top."""
    fig, ax = plt.subplots()
    ax.imshow(matrix)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1), ticklabels=("x", "y"))
    ax.yaxis.set(ticks=(0, 1), ticklabels=("x", "y"))
    ax.set_ylim(1.5, -0.5)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, matrix[i, j], ha="center", va="center", color="w")
    plt.show()


def main():
    np.random.seed(seed=0)
    x = np.arange(21)
    y = 5 + 2 * x + 2 * np.random.randn(21)

    draw_heatmap(np.cov(x, y).round(decimals=2))
    draw_heatmap(np.corrcoef(x, y).round(decimals=2))


if __name__ == "__main__":
    main()
