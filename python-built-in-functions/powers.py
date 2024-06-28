import timeit

base = 2
exp = 1000000
mod = 1000000

print(
    timeit.timeit("pow(base, exp) % mod", globals=globals(), number=10) * 1000
)

print(
    timeit.timeit("pow(base, exp, mod)", globals=globals(), number=10) * 1000
)
