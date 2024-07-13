# What Is the __pycache__ Folder in Python?

Source code, shell scripts, and example projects for the [What Is the `__pycache__` Folder in Python?](https://realpython.com/python-pycache/) tutorial on Real Python.

## Setup

You don't need to create a virtual environments because you won't be installing anything.

## Cleanup Scripts

To recursively remove the `__pycache__` folders on macOS and Linux:

```shell
$ ./pyclean.sh
```

To do the same on Windows in PowerShell:

```shell
PS> .\pyclean.ps1
```

## X-Ray of `.pyc` Files

Compile sample bytecode into timestamp-based `.pyc` files:

```shell
$ ./pyclean.sh
$ python -m compileall --invalidation-mode timestamp example-2/
$ python xray.py example-2/__pycache__/arithmetic*.pyc
{'magic_number': b'\xcb\r\r\n',
 'magic_int': 3531,
 'python_version': '3.12',
 'bit_field': 0,
 'pyc_type': <PycInvalidationMode.TIMESTAMP: 1>,
 'timestamp': datetime.datetime(2024, 3, 28, 17, 8, 22, tzinfo=datetime.timezone.utc),
 'file_size': 32}
```

Compile sample bytecode into unchecked hash-based `.pyc` files:

```shell
$ ./pyclean.sh
$ python -m compileall --invalidation-mode unchecked-hash example-2/
$ python xray.py example-2/__pycache__/arithmetic*.pyc
{'magic_number': b'\xcb\r\r\n',
 'magic_int': 3531,
 'python_version': '3.12',
 'bit_field': 1,
 'pyc_type': <PycInvalidationMode.UNCHECKED_HASH: 3>,
 'hash_value': b'\xf3\xdd\x87j\x8d>\x0e)'}
```

Compile sample bytecode into checked hash-based `.pyc` files:

```shell
$ ./pyclean.sh
$ python -m compileall --invalidation-mode checked-hash example-2/
$ python xray.py example-2/__pycache__/arithmetic*.pyc
{'magic_number': b'\xcb\r\r\n',
 'magic_int': 3531,
 'python_version': '3.12',
 'bit_field': 3,
 'pyc_type': <PycInvalidationMode.CHECKED_HASH: 2>,
 'hash_value': b'\xf3\xdd\x87j\x8d>\x0e)'}
```

## Java Bytecode Compiler

Compile the source code upfront and run the resulting class file:

```shell
$ javac Calculator.java
$ time java Calculator
```

Let the `java` command handle the compilation:

```shell
$ time java Calculator.java
```
