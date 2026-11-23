# Conditional Statements in Python

This folder provides the code examples for the Real Python tutorial [Conditional Statements in Python](https://realpython.com/python-conditional-statements/).

You can run all of the scripts directly by specifying their name:

```sh
$ python <filename>.py
```

The scripts only use the standard library, so there's nothing to install.

## The Scripts

Each script collects one section of the tutorial, in the order the tutorial presents it:

| Script | Tutorial section |
| --- | --- |
| [`if_statement.py`](./if_statement.py) | Introduction to the `if` Statement |
| [`foo.py`](./foo.py) | Python: It's All About the Indentation (the script file `foo.py`) |
| [`blocks.py`](./blocks.py) | Python: It's All About the Indentation (the script file `blocks.py`) |
| [`else_elif.py`](./else_elif.py) | The `else` and `elif` Clauses |
| [`one_line_if.py`](./one_line_if.py) | One-Line `if` Statements |
| [`conditional_expressions.py`](./conditional_expressions.py) | Conditional Expressions (Python's Ternary Operator) |
| [`pass_statement.py`](./pass_statement.py) | The Python `pass` Statement |

## A Note on the Examples

Most of the tutorial's examples are REPL sessions. In the scripts, values that the REPL would echo are passed to `print()`, and strings are printed with `repr()` so that the output matches the quoted form the REPL shows.

A few examples deliberately keep their original layout, with the formatter switched off: the commented "Does line execute?" table in `blocks.py`, the one-line `if` statements, and the chained conditional expression. Formatting them would remove what those examples demonstrate. PEP 8 recommends against one-line `if` statements, so don't copy that style into your own code.

The tutorial also shows a script that raises an `IndentationError` because its `if` block is empty. It can't run, so it isn't reproduced here. `pass_statement.py` is the fixed version.
