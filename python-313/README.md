# Python 3.13 Demos

This repository contains sample code and data files that demonstrate some of the new features in Python 3.13.

## Introduction

You need Python 3.13 installed to run these examples. See the following tutorial instructions:

- [How Can You Install a Pre-Release Version of Python](https://realpython.com/python-pre-release/)

Note that for testing the free-threading and JIT features, you'll need to build Python from source code with additional compiler flags enabled, as [explained in the tutorial](https://realpython.com/python313-free-threading-jit/#get-your-hands-on-the-new-features). Alternatively, you can run benchmarks using Docker containers as [explained below](#free-threading-and-jit).

You can learn more about Python 3.13's new features in the following Real Python tutorials:

- [Python 3.13: Cool New Features for You to Try](https://realpython.com/python313-new-features/)
- [Python 3.13 Preview: Free Threading and a JIT Compiler](https://realpython.com/python313-free-threading-jit/) 
- [Python 3.13 Preview: A Modern REPL](https://realpython.com/python313-repl)

You'll find examples from these tutorials in this repository.

## Examples

This section only contains brief instructions on how you can run the examples. See the tutorials for technical details.

### REPL

The following examples are used to demonstrate different features of the new REPL:

- [`tab_completion.py`](repl/tab_completion.py)
- [`multiline_editing.py`](repl/multiline_editing.py)
- [`power_factory.py](repl/power_factory.py)
- [`guessing_game.py](repl/guessing_game.py)
- [`roll_dice.py`](repl/roll_dice.py)

### Error messages

Run the scripts in the `errors/` folder to see different error messages produced by Python 3.13.

### Free-Threading and JIT

You need to enable a few build options to try out the free-threading and JIT features in Python 3.13. You can find more information in the dedicated [README file](free-threading-jit/README.md).

## Static typing

Run the scripts in the `typing/` folder to try out the new static typing features.

## Other features

The following scripts illustrate other new features in Python 3.13:

- [`replace.py`](replace.py): Use `copy.replace()` to update immutable data structures.
- [`paths.py`](paths.py) and [`music/`](music/): Glob patterns are more consistent.
- [`docstrings.py`](docstrings.py): Common leading whitespace in docstrings is stripped.

## Authors

- **Bartosz Zaczyński**, E-mail: [bartosz@realpython.com](bartosz@realpython.com)
- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.
