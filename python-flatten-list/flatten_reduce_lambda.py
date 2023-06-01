from functools import reduce


def flatten_reduce_lambda(matrix):
    return list(reduce(lambda x, y: x + y, matrix, []))
