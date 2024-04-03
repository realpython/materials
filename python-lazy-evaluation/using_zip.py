"""
Exploring 'zip()' lazy evaluation
"""

import random

names = ["Sarah", "Matt", "Jim", "Denise", "Kate"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
random.shuffle(names)
print(names)

# Using 'zip()' in a 'for' loop
for day, name in zip(weekdays, names):
    print(f"{day}: {name}")

# Using 'zip()' with 'next()'
day_name_pairs = zip(weekdays, names)
print(next(day_name_pairs))
print(next(day_name_pairs))

# Update third name
names[2] = "The Coffee Robot"
print(next(day_name_pairs))
# Output: ('Wednesday', 'The Coffee Robot')
