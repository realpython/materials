# Thonny: The Beginner-Friendly Python Editor

This folder provides the code examples for the Real Python tutorial [Thonny: The Beginner-Friendly Python Editor](https://realpython.com/python-thonny/).

The tutorial is about [Thonny](https://thonny.org/), the Python editor. Thonny itself isn't listed in `requirements.txt` because it's the editor you use to open and run these files. The tutorial uses Thonny 5.0.

## Installation

The calculator examples use the third-party [`simplecalculator`](https://pypi.org/project/simplecalculator/) package. You can install it with Thonny's package manager (*Tools* > *Manage Packages...*), as shown in the tutorial, or from the command line:

```console
$ python -m pip install -r requirements.txt
```

The code requires Python 3.6 or later.

## Factorial

- [`factorial.py`](factorial.py): A recursive factorial function that prints `factorial(3)`. Use it to try out running and stepping through code in Thonny.
- [`factorial_100.py`](factorial_100.py): The same program calling `factorial(100)`, which takes a long time to step through and is a good reason to use the stop button.

```console
$ python factorial.py
6
```

## Simple Calculator

- [`calculations_v1.py`](calculations_v1.py): The first version of `calculations.py`, which uses `SimpleCalculator` to compute `2 * 2`.
- [`calculations.py`](calculations.py): The updated version with a bug in `create_add_string()`. Open it in Thonny and use the debugger to find the bug.
- [`calculations_fixed.py`](calculations_fixed.py): The same program with the bug fixed, so you can check your solution.

```console
$ python calculations_v1.py
4.0

$ python calculations.py
0

$ python calculations_fixed.py
4.0
```
