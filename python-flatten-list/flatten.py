from functools import reduce
from itertools import chain
from operator import add, concat, iconcat


def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list


def flatten_concatenation(matrix):
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list


def flatten_comprehension(matrix):
    return [item for row in matrix for item in row]


def flatten_chain(matrix):
    return list(chain.from_iterable(matrix))


def flatten_reduce_lambda(matrix):
    return list(reduce(lambda x, y: x + y, matrix, []))


def flatten_reduce_add(matrix):
    return reduce(add, matrix, [])


def flatten_reduce_concat(matrix):
    return reduce(concat, matrix, [])


def flatten_reduce_iconcat(matrix):
    return reduce(iconcat, matrix, [])


def flatten_sum(matrix):
    return sum(matrix, [])
