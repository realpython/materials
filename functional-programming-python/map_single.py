"""
Examples of using `map()` with a single iterable.
"""


def reverse(s):
    return s[::-1]


print(reverse("I am a string"))

animals = ["cat", "dog", "hedgehog", "gecko"]

# Use `map()` to create an iterator.
iterator = map(reverse, animals)
print(iterator)

# Consume the iterator with a for loop.
iterator = map(reverse, animals)
for animal in iterator:
    print(animal)

# Consume the iterator with a call to `list()`.
iterator = map(reverse, animals)
print(list(iterator))

# Use a lambda expression.
iterator = map(lambda s: s[::-1], animals)
print(list(iterator))

# All the code in a single line.
print(list(map(lambda s: s[::-1], ["cat", "dog", "hedgehog", "gecko"])))

# Convert integers to strings before concatenating them.
print("+".join(map(str, [1, 2, 3, 4, 5])))
