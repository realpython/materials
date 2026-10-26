# Python Debugging With Pdb

This folder provides the code examples for the Real Python tutorial [Python Debugging With Pdb](https://realpython.com/python-debugging-pdb/).

## Setup

The examples only use Python's standard library, so there's nothing to install. The debugger sessions in the tutorial were recorded with Python 3.14. Older versions of Python print slightly different output. For example, `pdb.set_trace()` only stops on its own line starting with Python 3.13.

On macOS and Linux, you can run the main scripts directly after making them executable:

```sh
$ chmod +x example*.py
```

On Windows, run them with `python` instead, for example `python example1.py`.

## Usage

Each script calls `import pdb; pdb.set_trace()` to drop you into the debugger:

```sh
$ ./example1.py
```

| Script | Tutorial section |
| --- | --- |
| `example1.py` | Getting Started: Printing a Variable's Value |
| `example2.py` | Printing Expressions |
| `example3.py` | Stepping Through Code |
| `example4.py`, `util.py` | Using Breakpoints |
| `example4unt.py` | Continuing Execution |
| `example4display.py` | Displaying Expressions |
| `example5.py`, `fileutil.py` | Python Caller ID |

Type `c` at the `(Pdb)` prompt to continue running the script, or `q` to quit the debugger.

**Note:** The scripts keep the tutorial's `import pdb; pdb.set_trace()` one-liners and line layout so that the line numbers match the debugger sessions in the tutorial. That's why this folder is excluded from the repository's Ruff checks.
