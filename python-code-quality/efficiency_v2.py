from time import perf_counter

cache = {0: 0, 1: 1}


def fibonacci_of(n):
    if n in cache:
        return cache[n]
    cache[n] = fibonacci_of(n - 1) + fibonacci_of(n - 2)
    return cache[n]


start = perf_counter()
[fibonacci_of(n) for n in range(35)]
end = perf_counter()

print(f"Execution time: {end - start:.2f} seconds")
