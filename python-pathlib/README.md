# Python's pathlib Module: Taming the File System

This folder provides the code examples for the Real Python tutorial [Python's pathlib Module: Taming the File System](https://realpython.com/python-pathlib/).

## Setup

You need Python 3.9 or later. The `pathlib` module is part of the standard library, so there's nothing to install.

Run the scripts from inside this folder, because several of them read and write files relative to the current working directory.

## Usage

Print the folder that contains the script:

```console
$ python hello.py
You can find me here: /path/to/python-pathlib!
```

Read the groceries from `shopping_list.md`:

```console
$ python read_shopping_list.py
* Banana
* Apple
* Peach
* Chocolate
* Nougat Bits
```

Write the groceries to a new file, `plain_list.md`:

```console
$ python write_plain_shoppinglist.py
```

The `display_dir_tree.py` and `unique_path.py` modules define functions that you can import in a REPL session:

```pycon
>>> from pathlib import Path
>>> from display_dir_tree import tree
>>> tree(Path.cwd())
+ /path/to/python-pathlib
    + README.md
    + display_dir_tree.py
    ...

>>> from unique_path import unique_path
>>> unique_path(Path.cwd(), "test{:03d}.txt")
PosixPath('/path/to/python-pathlib/test001.txt')
```
