"""
Examples of using `reduce()` with two arguments.
"""

from functools import reduce


# Sum elements in an iterable.
def add_two_values(x, y):
    return x + y


print(reduce(add_two_values, [1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5]))


# Concatenate strings.
print(reduce(add_two_values, ["cat", "dog", "hedgehog", "gecko"]))
print("".join(["cat", "dog", "hedgehog", "gecko"]))


# Calculate the factorial with `reduce()`.
def multiply(x, y):
    return x * y


def factorial_with_reduce(n):
    return reduce(multiply, range(1, n + 1))


print(factorial_with_reduce(4))  # 1 * 2 * 3 * 4
print(factorial_with_reduce(6))  # 1 * 2 * 3 * 4 * 5 * 6


# Calculate the factorial with `math.factorial()`.
from math import factorial  # noqa E402

print(factorial(4))
print(factorial(6))


# Identify the maximum value.
print(max([23, 49, 6, 32]))


def greater(x, y):
    return x if x > y else y


print(reduce(greater, [23, 49, 6, 32]))


# Use lambda expressions to complete the tasks.
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x + y, ["cat", "dog", "hedgehog", "gecko"]))
print(reduce((lambda x, y: x if x > y else y), [23, 49, 6, 32]))
