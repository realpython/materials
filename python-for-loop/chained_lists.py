from itertools import chain

first = [7, 6, 1]
second = [4, 1]
third = [8, 0, 6]

for value in chain(first, second, third):
    print(value**2)
