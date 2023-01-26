from random import randint

import matplotlib.pyplot as plt
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
)


data.plot(relative_to=3, logy=True)

plt.gcf().set_size_inches(12, 7)
plt.subplots_adjust(left=0.2, right=0.8, top=0.85, bottom=0.15)
plt.savefig("plot_sorting_relative_to.png", transparent=True)
