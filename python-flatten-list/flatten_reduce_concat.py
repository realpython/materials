from functools import reduce
from operator import concat


def flatten_reduce_concat(matrix):
    return reduce(concat, matrix, [])
