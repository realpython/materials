# Recursion in Python: An Introduction

This folder provides the code examples for the Real Python tutorial [Recursion in Python: An Introduction](https://realpython.com/python-recursion/).

The code requires Python 3.6 or later and has no third-party dependencies.

## Infinite Recursion

- `infinite_recursion.py`: A function that calls itself without a base case. Running it raises a `RecursionError`.

## Count Down to Zero

- `countdown_recursive.py`: Recursive `countdown()` with an explicit base case and recursive call
- `countdown_concise.py`: A more concise recursive `countdown()`
- `countdown_iterative.py`: A non-recursive `countdown()` that uses a `while` loop

```console
$ python countdown_recursive.py
5
4
3
2
1
0
```

## Calculate Factorial

- `factorial_recursive.py`: Recursive `factorial()`
- `factorial_recursive_verbose.py`: Recursive `factorial()` with `print()` calls that trace the calls and return values
- `factorial_iterative.py`: Iterative `factorial()` that uses a `for` loop
- `factorial_reduce.py`: `factorial()` implemented with `functools.reduce()`
- `factorial_timing.py`: Compares the speed of the recursive, iterative, `reduce()`, and `math.factorial()` implementations with `timeit()`. It runs each one ten million times, so expect it to take a while.

```pycon
>>> from factorial_recursive_verbose import factorial
>>> factorial(4)
factorial() called with n = 4
factorial() called with n = 3
factorial() called with n = 2
factorial() called with n = 1
-> factorial(1) returns 1
-> factorial(2) returns 2
-> factorial(3) returns 6
-> factorial(4) returns 24
24
```

## Traverse a Nested List

- `names.py`: The nested `names` list used in the examples
- `count_leaf_items_recursive.py`: Recursive `count_leaf_items()`
- `count_leaf_items_verbose.py`: Recursive `count_leaf_items()` with `print()` calls that trace the traversal
- `count_leaf_items_iterative.py`: Non-recursive `count_leaf_items()` that uses a stack

```pycon
>>> from names import names
>>> from count_leaf_items_recursive import count_leaf_items
>>> count_leaf_items([1, [2.1, 2.2], 3])
4
>>> count_leaf_items(names)
10
```

## Detect Palindromes

- `palindrome_slicing.py`: `is_palindrome()` that compares a word to its reversed slice
- `palindrome_recursive.py`: Recursive `is_palindrome()`

```pycon
>>> from palindrome_recursive import is_palindrome
>>> is_palindrome("racecar")
True
>>> is_palindrome("troglodyte")
False
```

## Sort With Quicksort

- `quicksort.py`: Recursive `quicksort()` with median-of-three pivot selection, plus `get_random_numbers()` for generating test data

```pycon
>>> from quicksort import quicksort, get_random_numbers
>>> quicksort([10, -3, 21, 6, -8])
[-8, -3, 6, 10, 21]
>>> numbers = get_random_numbers(15, -50, 50)
>>> quicksort(numbers) == sorted(numbers)
True
```
