# Bitwise Operators in Python

Source code of the least-significant bit steganography example from the [Bitwise Operators in Python](https://realpython.com/python-bitwise-operators/) tutorial.  

## Installation

There are no external dependencies except for a Python interpreter. You can install this project by creating a new [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), activating it, and installing the Python package:

```shell
$ python -m venv venv/
$ source venv/bin/activate
(venv) python -m pip install .
```

## Running

Once the project is installed within your virtual environment, you can use the `stegano` command:

```shell
$ stegano /path/to/bitmap (--encode /path/to/file | --decode | --erase)
```

For example, to extract a secret file from the attached bitmap, type the following:

```shell
$ stegano example.bmp -d
Extracted a secret file: podcast.mp4
```
