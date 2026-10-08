"""Visualize raw numerical arrays as colored grids.

Covers the "A Burst of Color: imshow() and matshow()" section of
https://realpython.com/python-matplotlib-guide/
"""

import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
import numpy as np

np.random.seed(444)


def main():
    # Two distinct grids, built with some fancy NumPy indexing.
    x = np.diag(np.arange(2, 12))[::-1]
    x[np.diag_indices_from(x[::-1])] = np.arange(2, 12)
    x2 = np.arange(x.size).reshape(x.shape)

    # Toggle "off" all axis labels and ticks with a dict comprehension.
    sides = ("left", "right", "top", "bottom")
    nolabels = {s: False for s in sides}
    nolabels.update({"label%s" % s: False for s in sides})
    print(nolabels)

    with plt.rc_context(rc={"axes.grid": False}):
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
        ax1.matshow(x)
        img2 = ax2.matshow(x2, cmap="RdYlGn_r")
        for ax in (ax1, ax2):
            ax.tick_params(axis="both", which="both", **nolabels)
        for i, j in zip(*x.nonzero()):
            ax1.text(j, i, x[i, j], color="white", ha="center", va="center")

        # The colorbar needs a new Axes within `fig`.
        divider = make_axes_locatable(ax2)
        cax = divider.append_axes("right", size="5%", pad=0)
        plt.colorbar(img2, cax=cax, ax=[ax1, ax2])
        fig.suptitle("Heatmaps with `Axes.matshow`", fontsize=16)

    plt.show()


if __name__ == "__main__":
    main()
