from functools import reduce


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])


if __name__ == "__main__":
    print(factorial(4))
