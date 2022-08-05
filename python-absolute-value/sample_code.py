import math
from decimal import Decimal
from fractions import Fraction
from math import sqrt


class VectorBound:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __abs__(self):
        origin = [0] * len(self.coordinates)
        return math.dist(origin, self.coordinates)


class VectorFree:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __abs__(self):
        return math.hypot(*self.coordinates)


def absolute_value_piecewise(x):
    if x >= 0:
        return x
    else:
        return -x


def absolute_value_piecewise_conditional_expression(x):
    return x if x >= 0 else -x


def absolute_value_algebraic(x):
    return sqrt(pow(x, 2))


def absolute_value_algebraic_exponents(x):
    return (x**2) ** 0.5


def absolute_value_silly(x):
    return float(str(x).replace("-", ""))


if __name__ == "__main__":
    print(f"{absolute_value_piecewise(-12) = }")
    print(f"{absolute_value_piecewise_conditional_expression(-12) = }")
    print(f"{absolute_value_algebraic(-12) = }")
    print(f"{absolute_value_algebraic_exponents(-12) = }")
    print(f"{absolute_value_silly(-12) = }")

    print(f"{abs(-12) = }")
    print(f"{abs(-12.0) = }")
    print(f"{abs(complex(3, 2)) = }")
    print(f"{abs(Fraction('-3/4')) = }")
    print(f"{abs(Decimal('-0.75')) = }")

    print(f"{abs(VectorBound(0.42, 1.5, 0.87)) = }")
    print(f"{abs(VectorFree(0.42, 1.5, 0.87)) = }")
