"""Statements, the basic units of instruction in a Python program.

Code from the "Python Statements" section of the tutorial.

The formatter is switched off in this folder on purpose: this tutorial is
about lexical structure, so the exact line layout, whitespace, and quoting
of every example below is the lesson, not incidental style.
"""

# fmt: off
print('Hello, World!')

x = [1, 2, 3]
print(x[1:2])

# At the REPL a bare expression displays its value. In a script file it does
# nothing at all, so you need print() to see the result.
print(repr('foobar'[2:5]))
# fmt: on
