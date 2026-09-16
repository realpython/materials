"""Configure matplotlib styles and rc parameters.

Covers "Appendix A: Configuration and Styling" of
https://realpython.com/python-matplotlib-guide/
"""

import matplotlib.pyplot as plt


def main():
    # All of the module objects starting with "rc" are a means to
    # interact with your plot styles and settings.
    print([attr for attr in dir(plt) if attr.startswith("rc")])

    # These two syntaxes are equivalent for adjusting settings.
    plt.rc("lines", linewidth=2, color="r")  # Syntax 1

    plt.rcParams["lines.linewidth"] = 2  # Syntax 2
    plt.rcParams["lines.color"] = "r"

    # A style is just a predefined cluster of custom settings.
    print(plt.style.available)
    plt.style.use("fivethirtyeight")


if __name__ == "__main__":
    main()
