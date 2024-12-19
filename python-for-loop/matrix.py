from itertools import chain

matrix = [
    [9, 3, 8],
    [4, 5, 2],
    [6, 4, 3],
]

for value in chain(*matrix):
    print(value**2)
