from functools import reduce
from operator import add


def flatten_reduce_add(matrix):
    return reduce(add, matrix, [])
