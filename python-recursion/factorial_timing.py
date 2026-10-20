from timeit import timeit

recursive_setup = """
print("Recursive:")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
"""

iterative_setup = """
print("Iterative:")
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
"""

reduce_setup = """
from functools import reduce
print("reduce():")
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
"""

math_setup = """
print("math.factorial():")
from math import factorial
"""

if __name__ == "__main__":
    for setup_string in (
        recursive_setup,
        iterative_setup,
        reduce_setup,
        math_setup,
    ):
        print(timeit("factorial(4)", setup=setup_string, number=10000000))
