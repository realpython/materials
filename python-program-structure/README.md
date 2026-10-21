# Python Program Lexical Structure

This folder provides the code examples for the Real Python tutorial [Python Program Lexical Structure](https://realpython.com/python-program-structure/).

You can run all of the scripts directly by specifying their name:

```sh
$ python <filename>.py
```

The scripts only use the standard library, so there's nothing to install.

## The Scripts

Each script collects one section of the tutorial, in the order the tutorial presents it:

| Script | Tutorial section |
| --- | --- |
| [`statements.py`](./statements.py) | Python Statements |
| [`long_statements.py`](./long_statements.py) | Line Continuation |
| [`implicit_line_continuation.py`](./implicit_line_continuation.py) | Implicit Line Continuation |
| [`explicit_line_continuation.py`](./explicit_line_continuation.py) | Explicit Line Continuation |
| [`multiple_statements.py`](./multiple_statements.py) | Multiple Statements Per Line |
| [`comments.py`](./comments.py) | Comments |
| [`foo.py`](./foo.py) | Comments (the script file shown in the tutorial) |
| [`whitespace.py`](./whitespace.py) | Whitespace |

## A Note on the Examples

Nearly all of the tutorial's examples are REPL sessions. They've been turned into runnable scripts here, which means two small changes:

- Where the REPL echoed a value, the script calls `print()` so that you see the same result. String values are printed with `repr()` so that the output matches the quoted form the REPL displays.
- The code is otherwise copied verbatim, including the tutorial's single quotes and its deliberately cramped or deliberately sprawling line layouts.

That second point is why every script switches the formatter off with `# fmt: off`. This tutorial is *about* lexical structure, so line layout, whitespace, and quoting are the subject matter. Reformatting the examples would join the continued lines, split the semicolons, and pad out the whitespace, which would delete the very thing each example is demonstrating. For the same reason, the two semicolon examples carry a `# noqa: E702`.

The tutorial also shows a number of deliberate errors: unterminated statements, a backslash followed by a space, `sin`, `is20`, `notin`, and an unexpected indent. Those blocks can't run, so they aren't reproduced as code. Each script's docstring names the ones its section skips.

The tutorial's final code section, "Whitespace as Indentation," is not represented by a script. Its only Python example is a single `print('foo')` call and an `IndentationError`.
