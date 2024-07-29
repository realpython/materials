"""
Example implementations of using `reduce()` to create
functional versions of `map()` and `filter()`.
"""

# Compare `map()` to `custom_map()`.
numbers = [1, 2, 3, 4, 5]

print(list(map(str, numbers)))


def custom_map(function, iterable):
    from functools import reduce

    return reduce(
        lambda items, value: items + [function(value)],
        iterable,
        [],
    )


print(list(custom_map(str, numbers)))


# Compare `filter()` to `custom_filter()`.
numbers = list(range(10))


def is_even(x):
    return x % 2 == 0


print(list(filter(is_even, numbers)))


def custom_filter(function, iterable):
    from functools import reduce

    return reduce(
        lambda items, value: items + [value] if function(value) else items,
        iterable,
        [],
    )


print(list(custom_filter(is_even, numbers)))
