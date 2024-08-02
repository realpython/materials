"""
Examples of using a function object as an argument.
"""

animals = ["ferret", "vole", "dog", "gecko"]
print(sorted(animals))

animals = ["ferret", "vole", "dog", "gecko"]
print(sorted(animals, key=len))

animals = ["ferret", "vole", "dog", "gecko"]
print(sorted(animals, key=len, reverse=True))


def reverse_len(s):
    return -len(s)


print(sorted(animals, key=reverse_len))

# Using a lambda expression
print(sorted(animals, key=lambda s: -len(s)))
