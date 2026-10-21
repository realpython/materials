"""Traverse the nested objects that make up a matplotlib graphic.

Covers the "The Matplotlib Object Hierarchy" section of
https://realpython.com/python-matplotlib-guide/
"""

import matplotlib.pyplot as plt


def main():
    # A Figure is the outermost container for a matplotlib graphic.
    fig, _ = plt.subplots()
    print(type(fig))

    # Attribute notation walks down the hierarchy: Figure -> Axes ->
    # yaxis -> major ticks.
    one_tick = fig.axes[0].yaxis.get_major_ticks()[0]
    print(type(one_tick))


if __name__ == "__main__":
    main()
