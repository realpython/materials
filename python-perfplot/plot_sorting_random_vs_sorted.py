from random import randint

import perfplot

from sorting import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    tim_sort,
    python_built_in_sort,
)


def random_list(n):
    return [randint(0, n) for _ in range(n)]


def sorted_list(n):
    return list(range(n))


def nearly_sorted(n):
    return [1, *list(range(n - 1))]


def nearly_sorted_alt(n):
    return [n, *list(range(n - 1))]


def reverse_list(n):
    return list(range(n - 1, -1, -1))


for setup_f in [
    random_list,
    sorted_list,
    nearly_sorted,
    nearly_sorted_alt,
    reverse_list,
]:
    data = perfplot.bench(
        n_range=[2**n for n in range(20)],
        setup=setup_f,
        kernels=[
            bubble_sort,
            insertion_sort,
            merge_sort,
            quick_sort,
            tim_sort,
            python_built_in_sort,
        ],
        title=setup_f.__name__,
    )

    data.save(f"{setup_f.__name__}.png")
