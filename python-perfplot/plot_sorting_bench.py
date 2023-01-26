from random import randint

import perfplot

from sorting import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    python_built_in_sort,
    quick_sort,
    tim_sort,
)

data = perfplot.bench(
    n_range=[2**n for n in range(10)],
    setup=lambda n: [randint(0, 1000) for _ in range(n)],
    kernels=[
        bubble_sort,
        insertion_sort,
        merge_sort,
        quick_sort,
        tim_sort,
        python_built_in_sort,
    ],
)

data.save("sorting_algos_log_x.png", logx=True)
data.save("sorting_algos_linear_x.png", logx=False)
