from functools import reduce
from itertools import chain
from operator import add, concat, iconcat


def flatten_comprehension(matrix):
    return [item for row in matrix for item in row]


def flatten_concatenation(matrix):
    flat = []
    for row in matrix:
        flat += row
    return flat


def flatten_extend(matrix):
    flat = []
    for row in matrix:
        flat.extend(row)
    return flat


def flatten_itertools_chain(matrix):
    return list(chain.from_iterable(matrix))


def flatten_reduce_add(matrix):
    return reduce(add, matrix, [])


def flatten_reduce_concat(matrix):
    return reduce(concat, matrix, [])


def flatten_reduce_iconcat(matrix):
    return reduce(iconcat, matrix, [])


def flatten_reduce_lambda(matrix):
    return list(reduce(lambda x, y: x + y, matrix, []))


def flatten_sum(matrix):
    return sum(matrix, [])
