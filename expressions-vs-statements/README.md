# Expression vs Statement in Python: What's the Difference?

This folder contains sample code from the Real Python tutorial [Expression vs Statement in Python: What's the Difference?](https://realpython.com/python-expression-vs-statement/)

## Code Inspector

Identify whether a piece of Python code is an expression or a statement:

```shell
$ python code_inspector.py
Type a Python code snippet or leave empty to exit.
>>> yield
statement
>>> (yield)
expression
>>> 2 +
invalid
```

## GUI App

Register a lambda expression as a callback, which delegates to a function with statements:

```shell
$ python gui_app.py
```

## Echo Program

Compile with a C compiler and pipe stdin to the echo program:

```shell
$ gcc echo.c -o echo.x
$ echo "Hello, World!" | ./echo.x
Hello, World!
```

## HEX Reader

Read a binary file and display its bytes in hexadecimal format:

```shell
$ python hex_reader.py /path/to/HelloJava.class --columns 8
ca fe ba be 00 00 00 41
00 0f 0a 00 02 00 03 07
00 04 0c 00 05 00 06 01
(...)
```

## Generators

Generate a random signal and use a low-pass filter to make it smooth:

```shell
$ python generators.py 
-0.96: -0.96
-0.81: -0.89
-0.52: -0.67
 0.22: -0.15
 0.51:  0.37
 0.40:  0.46
-0.08:  0.16
-0.24: -0.16
 0.80:  0.28
 0.47:  0.64
```
