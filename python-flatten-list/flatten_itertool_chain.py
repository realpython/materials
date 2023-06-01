from itertools import chain


def flatten_itertools_chain(matrix):
    return list(chain.from_iterable(matrix))
