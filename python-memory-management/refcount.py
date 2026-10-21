"""Watch the reference count of a list change, step by step.

Each step runs one of the tutorial's snippets and then prints
sys.getrefcount(numbers). Passing the object to getrefcount() adds a
temporary reference, so the printed value is one more than the
reference count in the tutorial's comments.

Keep this code at module level, as it is here. Starting with
Python 3.14, CPython can pass a function's local variables to
getrefcount() without adding that extra reference, so the same code
inside a function prints values that are one lower.
"""

import sys

numbers = [1, 2, 3]
# Reference count = 1
print("numbers = [1, 2, 3]")
print(f"  sys.getrefcount(numbers) = {sys.getrefcount(numbers)}")

more_numbers = numbers
# Reference count = 2
print("more_numbers = numbers")
print(f"  sys.getrefcount(numbers) = {sys.getrefcount(numbers)}")

total = sum(numbers)
# Passing numbers as an argument increases the reference count only
# while sum() runs. Once it returns, the reference count is 2 again.
print("total = sum(numbers)")
print(f"  sys.getrefcount(numbers) = {sys.getrefcount(numbers)}")

matrix = [numbers, numbers, numbers]
# The new list holds three more references: reference count = 5
print("matrix = [numbers, numbers, numbers]")
print(f"  sys.getrefcount(numbers) = {sys.getrefcount(numbers)}")
