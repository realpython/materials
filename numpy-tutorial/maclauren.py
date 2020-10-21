"""Estimates e^x^ by using an approximated Maclauren series."""

from math import e, factorial

import numpy as np

fac = np.vectorize(factorial)


def e_x(x, terms=10):
    """Approximates e^x^ using 'terms' terms of the Maclauren Series"""
    n = np.arange(terms)
    return np.sum((x ** n) / fac(n))


if __name__ == "__main__":
    print("Actual:", e ** 3)

    print("N (terms)\tMaclauren\tError")

    for n in range(1, 14):
        maclauren = e_x(3, terms=n)
        print(f"{n}\t\t{maclauren:.03f}\t\t{e**3 - maclauren:.03f}")


# Actual: 20.085536923187664
# N (terms) Maclauren Error
# 1         1.000     19.086
# 2         4.000     16.086
# 3         8.500     11.586
# 4        13.000      7.086
# 5        16.375      3.711
# 6        18.400      1.686
# 7        19.412      0.673
# 8        19.846      0.239
# 9        20.009      0.076
# 10       20.063      0.022
# 11       20.080      0.006
# 12       20.084      0.001
# 13       20.085      0.000
