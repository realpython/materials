print([2, 3] == [2, 3])
print((2, 3) == (2, 3))

print([5, 6, 7] < [7, 5, 6])
print((5, 6, 7) < (7, 5, 6))

print([4, 3, 2] < [4, 3, 2])
print((4, 3, 2) < (4, 3, 2))

# You can compare lists to tuples for equality...
print([2, 3] == (2, 3))
print([2, 3] != (2, 3))

# ...but the order comparisons raise a TypeError
try:
    print([2, 3] > (2, 3))
except TypeError as error:
    print(error)

try:
    print([2, 3] <= (2, 3))
except TypeError as error:
    print(error)

# Sequences of different lengths
print([5, 6, 7] < [8])
print((5, 6, 7) < (8,))

print([5, 6, 7] == [5])
print((5, 6, 7) == (5,))

print([5, 6, 7] > [5])
print((5, 6, 7) > (5,))
