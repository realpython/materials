"""
Exploring 'enumerate()' lazy evaluation
"""

import random

names = ["Sarah", "Matt", "Jim", "Denise", "Kate"]
random.shuffle(names)
print(names)

# Using `enumerate()` in a 'for' loop
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

# Using `enumerate()` with 'next()'
numbered_names = enumerate(names, start=1)
print(numbered_names)

print(next(numbered_names))
print(next(numbered_names))

# Update third name
names[2] = "The Coffee Robot"
print(next(numbered_names))
# Output: (3, 'The Coffee Robot')
