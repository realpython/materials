from cProfile import Profile
from pstats import SortKey, Stats


def fib(n):
    return n if n < 2 else fib(n - 2) + fib(n - 1)


with Profile() as profile:
    print(f"{fib(35) = }")
    Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats()
