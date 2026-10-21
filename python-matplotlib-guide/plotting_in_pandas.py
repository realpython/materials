"""Mix pandas plotting methods with traditional matplotlib calls.

Covers the "Plotting in Pandas" section of
https://realpython.com/python-matplotlib-guide/

The VIX series is downloaded from FRED at runtime, so this script needs
an internet connection.
"""

import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np
import pandas as pd

np.random.seed(444)


def series_introspection():
    """Show that pandas' plot() wraps the state-based plt.plot()."""
    s = pd.Series(np.arange(5), index=list("abcde"))
    ax = s.plot()

    print(type(ax))
    print(id(plt.gca()) == id(ax))


def volatility_regime():
    """Plot the moving average of the VIX, colored by regime state."""
    url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS"
    vix = (
        pd.read_csv(url, index_col=0, parse_dates=True, na_values=".")
        .squeeze("columns")
        .dropna()
    )
    ma = vix.rolling("90D").mean()
    state = pd.cut(ma, bins=[-np.inf, 14, 18, 24, np.inf], labels=range(4))

    cmap = plt.get_cmap("RdYlGn_r")
    ma.plot(
        color="black",
        linewidth=1.5,
        marker="",
        figsize=(8, 4),
        label="VIX 90d MA",
    )
    ax = plt.gca()  # Get the current Axes that ma.plot() references
    ax.set_xlabel("")
    ax.set_ylabel("90d moving average: CBOE VIX")
    ax.set_title("Volatility Regime State")
    ax.grid(False)
    ax.legend(loc="upper center")
    ax.set_xlim(xmin=ma.index[0], xmax=ma.index[-1])

    trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
    for i, color in enumerate(cmap([0.2, 0.4, 0.6, 0.8])):
        ax.fill_between(
            ma.index,
            0,
            1,
            where=state == i,
            facecolor=color,
            transform=trans,
        )
    ax.axhline(
        vix.mean(),
        linestyle="dashed",
        color="xkcd:dark grey",
        alpha=0.6,
        label="Full-period mean",
        marker="",
    )
    plt.show()


if __name__ == "__main__":
    for section in (series_introspection, volatility_regime):
        title = section.__name__.replace("_", " ").title()
        print(f"\n{title}\n{'-' * len(title)}")
        section()
