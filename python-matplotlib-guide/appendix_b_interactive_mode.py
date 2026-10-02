"""Toggle matplotlib's interactive mode on and off.

Covers "Appendix B: Interactive Mode" of
https://realpython.com/python-matplotlib-guide/

The tutorial runs these lines in an interactive session, where
interactive mode is already on, so the first value it prints is True.
Run as a script, matplotlib starts with interactive mode off, so the
first value below prints False.
"""

import matplotlib.pyplot as plt
import numpy as np


def main():
    print(plt.rcParams["interactive"])  # or: plt.isinteractive()

    plt.ioff()
    print(plt.rcParams["interactive"])

    # With interactive mode off, plt.show() is what displays the figure.
    x = np.arange(-4, 5)
    y1 = x**2
    y2 = 10 / (x**2 + 1)
    fig, ax = plt.subplots()
    ax.plot(x, y1, "rx", x, y2, "b+", linestyle="solid")
    ax.fill_between(
        x, y1, y2, where=y2 > y1, interpolate=True, color="green", alpha=0.3
    )
    lgnd = ax.legend(["y1", "y2"], loc="upper center", shadow=True)
    lgnd.get_frame().set_facecolor("#ffb19a")
    plt.show()


if __name__ == "__main__":
    main()
