"""Draw ordinary and cumulative histograms.

Covers the "Histograms" section of https://realpython.com/python-statistics/
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")


def main():
    np.random.seed(seed=0)
    x = np.random.randn(1000)

    # np.histogram() gives you the same numbers that .hist() draws.
    hist, bin_edges = np.histogram(x, bins=10)
    print(f"{hist = }")
    print(f"{bin_edges = }")

    for cumulative in (False, True):
        fig, ax = plt.subplots()
        ax.hist(x, bin_edges, cumulative=cumulative)
        ax.set_xlabel("x")
        ax.set_ylabel("Frequency")
        plt.show()


if __name__ == "__main__":
    main()
