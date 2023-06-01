from timeit import timeit

from flatten_comprehension import flatten_comprehension
from flatten_concatenation import flatten_concatenation
from flatten_extend import flatten_extend
from flatten_itertool_chain import flatten_itertools_chain
from flatten_reduce_add import flatten_reduce_add
from flatten_reduce_concat import flatten_reduce_concat
from flatten_reduce_iconcat import flatten_reduce_iconcat
from flatten_reduce_lambda import flatten_reduce_lambda
from flatten_sum import flatten_sum

SIZE = 1000
TO_MS = 1000
FUNCTIONS = [
    flatten_comprehension,
    flatten_concatenation,
    flatten_extend,
    flatten_reduce_lambda,
    flatten_sum,
    flatten_itertools_chain,
    flatten_reduce_add,
    flatten_reduce_concat,
    flatten_reduce_iconcat,
]

matrix = [list(range(SIZE))] * SIZE

results = [
    (
        f"{func.__name__}()",
        timeit(f"{func(matrix)}", globals=globals(), number=1) * TO_MS,
    )
    for func in FUNCTIONS
]

print(f"Time to flatten a {SIZE}x{SIZE} matrix (in milliseconds):\n")

for func, time in sorted(results, key=lambda result: result[1]):
    print(f"{func:.<30}{time: >7.6f} ms")
