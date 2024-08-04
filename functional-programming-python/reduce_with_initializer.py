"""
Examples of using `reduce()` with an initializer value.
"""

from functools import reduce


def add_two_values(x, y):
    return x + y


# Initialize with the value `100`.
# (100 + 1 + 2 + 3 + 4 + 5)
print(reduce(add_two_values, [1, 2, 3, 4, 5], 100))

# Use a lambda expression.
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 100))

# Use `sum()` and add a value instead.
print(sum([1, 2, 3, 4, 5], start=100))
