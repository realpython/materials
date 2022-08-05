import math
from decimal import Decimal
from fractions import Fraction
from math import sqrt


class Vector1:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __abs__(self):
        origin = [0] * len(self.coordinates)
        return math.dist(origin, self.coordinates)


class Vector2:
    def __init__(self, *coordinates):
        self.coordinates = coordinates

    def __abs__(self):
        return math.hypot(*self.coordinates)


def absolute_value1(x):
    if x >= 0:
        return x
    else:
        return -x


def absolute_value2(x):
    return x if x >= 0 else -x


def absolute_value3(x):
    return sqrt(pow(x, 2))


def absolute_value4(x):
    return (x**2) ** 0.5


def absolute_value5(x):
    return float(str(x).replace("-", ""))


if __name__ == "__main__":
    print(f"{absolute_value1(-12) = }")
    print(f"{absolute_value2(-12) = }")
    print(f"{absolute_value3(-12) = }")
    print(f"{absolute_value4(-12) = }")
    print(f"{absolute_value5(-12) = }")

    print(f"{abs(-12) = }")
    print(f"{abs(-12.0) = }")
    print(f"{abs(complex(3, 2)) = }")
    print(f"{abs(Fraction('-3/4')) = }")
    print(f"{abs(Decimal('-0.75')) = }")

    print(f"{abs(Vector1(0.42, 1.5, 0.87)) = }")
    print(f"{abs(Vector2(0.42, 1.5, 0.87)) = }")

