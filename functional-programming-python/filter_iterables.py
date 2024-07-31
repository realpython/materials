"""
Example use cases of Python's `filter()` function.
"""


# Keep only high numbers.
def greater_than_100(x):
    return x > 100


print(list(filter(greater_than_100, [1, 111, 2, 222, 3, 333])))
print(list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333])))


# Filter out odd numbers.
def is_even(x):
    return x % 2 == 0


print(list(filter(is_even, range(10))))
print(list(filter(lambda x: x % 2 == 0, range(10))))

# Keep only uppercase strings.
animals = ["cat", "Cat", "CAT", "dog", "Dog", "DOG", "emu", "Emu", "EMU"]


def all_caps(s):
    return s.isupper()


print(list(filter(all_caps, animals)))
print(list(filter(lambda s: s.isupper(), animals)))

# Remove empty strings.
animals_and_empty_strings = ["", "cat", "dog", "", ""]

print(list(filter(lambda s: s, animals_and_empty_strings)))
