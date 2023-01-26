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

perfplot.live(
    n_range=[2**n for n in range(15)],
    setup=lambda n: [randint(0, 1_000) for _ in range(n)],
    kernels=[
        bubble_sort,
        insertion_sort,
        merge_sort,
        quick_sort,
        tim_sort,
        python_built_in_sort,
    ],
    logy=True,
    labels=[
        "bubble sort",
        "insertion sort",
        "merge sort",
        "quick sort",
        "tim sort",
        "built in sort",
    ],
    xlabel="Number of elements in list",
)
