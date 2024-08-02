"""
Examples of writing lambda expressions.
"""


# Reverse a string.
def reverse(s):
    return s[::-1]


print(reverse("I am a string"))

reverse = lambda s: s[::-1]  # noqa E731
print(reverse("I am a string"))

print((lambda s: s[::-1])("I am a string"))


# Calculate the average of three numbers.
print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(9, 6, 6))
print((lambda x1, x2, x3: (x1 + x2 + x3) / 3)(1.4, 1.1, 0.5))

# Return a fixed value.
forty_two_producer = lambda: 42  # noqa E731
print(forty_two_producer())

# Use a conditional expression.
print((lambda x: "even" if x % 2 == 0 else "odd")(2))
print((lambda x: "even" if x % 2 == 0 else "odd")(3))
