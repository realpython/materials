"""
Example implementations of using `reduce()` to create
functional versions of `map()` and `filter()`.
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Compare `map()` to `custom_map()`.
def custom_map(function, iterable):
    return reduce(
        lambda items, value: items + [function(value)],
        iterable,
        [],
    )


print(list(map(str, numbers)))
print(list(custom_map(str, numbers)))


# Compare `filter()` to `custom_filter()`.
def is_even(x):
    return x % 2 == 0


def custom_filter(function, iterable):
    return reduce(
        lambda items, value: items + [value] if function(value) else items,
        iterable,
        [],
    )


print(list(filter(is_even, numbers)))
print(list(custom_filter(is_even, numbers)))
