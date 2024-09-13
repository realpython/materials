from time import sleep
from timeit import timeit


def memoize(function):
    cache = {}

    def closure(number):
        if number not in cache:
            cache[number] = function(number)
        return cache[number]

    return closure


@memoize
def slow_operation(number):
    sleep(0.5)


exec_time = timeit(
    "[slow_operation(number) for number in [2, 3, 4, 2, 3, 4]]",
    globals=globals(),
    number=1,
)

print(f"Slow operation's time:   {exec_time:.2f} seconds.")
