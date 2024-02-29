import math

from decorators import debug

math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


if __name__ == "__main__":
    print(approximate_e(5))
