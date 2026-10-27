# Memory Management in Python

This folder provides the code examples for the Real Python tutorial [Memory Management in Python](https://realpython.com/python-memory-management/).

## Files

- `refcount.py`: Runs the tutorial's three reference-counting snippets in order and prints `sys.getrefcount(numbers)` after each step.

## Usage

```sh
$ python refcount.py
numbers = [1, 2, 3]
  sys.getrefcount(numbers) = 2
more_numbers = numbers
  sys.getrefcount(numbers) = 3
total = sum(numbers)
  sys.getrefcount(numbers) = 3
matrix = [numbers, numbers, numbers]
  sys.getrefcount(numbers) = 6
```

Each printed value is one more than the reference count described in the tutorial, because passing `numbers` to `sys.getrefcount()` temporarily adds a reference. Starting with Python 3.14, this extra reference may not appear when you call `sys.getrefcount()` on a local variable inside a function, so run the code at module level, as the script does, to see the same numbers.

## Requirements

The code runs on Python 3.6 or later.
