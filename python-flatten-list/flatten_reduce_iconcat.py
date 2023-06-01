from functools import reduce
from operator import iconcat


def flatten_reduce_iconcat(matrix):
    return reduce(iconcat, matrix, [])
