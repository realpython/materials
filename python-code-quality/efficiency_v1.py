from time import perf_counter


def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


start = perf_counter()
[fibonacci_of(n) for n in range(35)]
end = perf_counter()

print(f"Execution time: {end - start:.2f} seconds")
