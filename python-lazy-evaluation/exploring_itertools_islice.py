"""
Exploring the itertools module
"""

import itertools

numbers = [2, 4, 6, 8, 10]
standard_slice = numbers[1:4]
iterator_slice = itertools.islice(numbers, 1, 4)

# Change third element in numbers
numbers[2] = 999

print(numbers)

print("\nStandard slice:")
for number in standard_slice:
    print(number)

print("\nIterator slice:")
for number in iterator_slice:
    print(number)
