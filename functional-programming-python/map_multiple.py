"""
Example of using multiple iterables as arguments to `map()`.
"""


def add_three(a, b, c):
    return a + b + c


print(list(map(add_three, [1, 2, 3], [10, 20, 30], [100, 200, 300])))

# Using a lambda expression.
print(
    list(
        map(
            lambda a, b, c: a + b + c,
            [1, 2, 3, 4],
            [10, 20, 30, 40],
            [100, 200, 300, 400],
        )
    )
)
