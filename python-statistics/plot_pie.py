"""Draw a pie chart of three values.

Covers the "Pie Charts" section of https://realpython.com/python-statistics/
"""

import matplotlib.pyplot as plt

plt.style.use("ggplot")


def main():
    x, y, z = 128, 256, 1024

    fig, ax = plt.subplots()
    ax.pie((x, y, z), labels=("x", "y", "z"), autopct="%1.1f%%")
    plt.show()


if __name__ == "__main__":
    main()
