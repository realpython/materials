# Bitwise Operators in Python

Source code of the least-significant bit **steganography** example from the [Bitwise Operators in Python](https://realpython.com/python-bitwise-operators/) article.  

## Installation

There are no external dependencies except for a Python interpreter.

## Running

Change directory to the current folder, where this `README.md` file is located, and then execute Python module:

```shell
$ python -m stegano /path/to/bitmap (--encode /path/to/file | --decode | --erase)
```

For example, to extract a secret file from the attached bitmap, type the following:

```shell
$ python -m stegano example.bmp -d
Extracted a secret file: podcast.mp4
```
