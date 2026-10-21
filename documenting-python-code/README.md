# Documenting Python Code: A Complete Guide

This folder provides the code examples for the Real Python tutorial [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/).

## Installation

Only the spreadsheet examples need third-party packages. Install them into a virtual environment with:

```sh
$ python -m pip install -r requirements.txt
```

The standalone examples run on Python 3.6 or later. The spreadsheet examples use the pinned pandas version, which requires Python 3.11 or later.

## Files

- **`comments.py`**: Functions showing short and multi-line comments.
- **`type_hints.py`**: A function that uses type hints in place of comments.
- **`say_hello_v1.py`**: Sets a function's docstring by assigning to `__doc__`.
- **`say_hello_v2.py`**: Sets the same docstring with a string literal below the `def` line.
- **`simple_class.py`**: Shows where class and method docstrings go.
- **`animal.py`**: The `Animal` class with NumPy/SciPy-style class and method docstrings.
- **`spreadsheet_columns.py`**: A command-line script with a script docstring that prints a spreadsheet's column headers.
- **`docstring_formats.py`**: The spreadsheet function documented in the Google, reStructuredText, NumPy/SciPy, and Epytext formats.

## Usage

Inspect docstrings with `help()`:

```pycon
>>> from say_hello_v2 import say_hello
>>> help(say_hello)
Help on function say_hello in module say_hello_v2:

say_hello(name)
    A simple function that says hello... Richie style

>>> from animal import Animal
>>> Animal("dog", "woof").says()
A dog says woof
```

Print the column headers of a CSV or Excel spreadsheet:

```sh
$ python spreadsheet_columns.py people.xlsx
name
age
city
```

Run `python spreadsheet_columns.py -h` to see the script's docstring used as the help message, or run `python docstring_formats.py` to print the same docstring in all four formats.
