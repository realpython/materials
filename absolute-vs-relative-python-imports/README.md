# Absolute vs Relative Imports in Python

This folder provides the code examples for the Real Python tutorial [Absolute vs Relative Imports in Python](https://realpython.com/absolute-vs-relative-python-imports/).

The code requires Python 3.3 or later, because `package1/` has no `__init__.py` file and relies on [namespace packages](https://peps.python.org/pep-0420/).

## Example Project

The tutorial's `project/` tree comes in two parallel copies so you can compare both import styles:

- [`absolute/project/`](absolute/project/) uses absolute imports.
- [`relative/project/`](relative/project/) uses explicit relative imports.

Both copies contain the same files:

- `package1/module1.py`: Imports `function1` from `module2` and prints its result.
- `package1/module2.py`: Defines `function1()`.
- `package2/__init__.py`: Defines `class1`.
- `package2/module3.py`: Imports `class1` and `function2` and prints them.
- `package2/module4.py`: Part of the tutorial's tree, but empty because no example uses it.
- `package2/subpackage1/module5.py`: Defines `function2()`.
- `main.py`: Entry point that runs the imports. In `absolute/project/`, it also holds the tutorial's block of absolute import examples.

Run the examples from inside a `project/` folder so that `package1` and `package2` are importable:

```sh
$ cd absolute/project/
$ python main.py
Absolute imports:
Hello from function1() in package1/module2.py
<class1 from package2/__init__.py>
Hello from function2() in package2/subpackage1/module5.py

module1.main():
Hello from function1() in package1/module2.py

module3.main():
<class1 from package2/__init__.py>
Hello from function2() in package2/subpackage1/module5.py
```

You can also run a single module with the `-m` switch, which works for both copies:

```sh
$ cd relative/project/
$ python -m package2.module3
<class1 from package2/__init__.py>
Hello from function2() in package2/subpackage1/module5.py
```

Running a module as a file path, such as `python package1/module1.py`, fails in both copies. The relative version raises `ImportError: attempted relative import with no known parent package`. The absolute version raises `ModuleNotFoundError` because `project/` isn't on the import path.

## Import Styling

- [`import_style.py`](import_style.py): The tutorial's example of PEP 8 import grouping and ordering.

This file is only a style reference and isn't meant to run. It imports third-party Flask packages and the placeholder modules `local_module` and `local_package`, which don't exist. A `# ruff: noqa: F401` comment at the top stops the linter from flagging the imports as unused.
