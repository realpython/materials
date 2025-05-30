import time


def fibonacci_of_v1(n):
    if n <= 1:
        return n
    return fibonacci_of_v1(n - 1) + fibonacci_of_v1(n - 2)


start = time.perf_counter()
fibonacci_of_v1(35)
end = time.perf_counter()
print(f"{end - start:.3f} seconds")


def fibonacci_of_v2(n):
    cache = fibonacci_of_v2.__dict__.setdefault("cache", {})
    if n in cache:
        return cache[n]
    cache[n] = n if n <= 1 else fibonacci_of_v2(n - 1) + fibonacci_of_v2(n - 2)
    return cache[n]


start = time.perf_counter()
fibonacci_of_v2(35)
end = time.perf_counter()
print(f"{end - start:.3f} seconds")
