"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Module-level tests:
>>> add(2, 4)
6.0
>>> subtract(5, 3)
2.0
>>> multiply(2.0, 4.0)
8.0
>>> divide(4.0, 2)
2.0
"""


def add(a, b):
    """Compute and return the sum of two numbers.

    Tests for add():
    >>> add(4.0, 2.0)
    6.0
    >>> add(4, 2)
    6.0
    """
    return float(a + b)


def subtract(a, b):
    """Calculate the difference of two numbers.

    Tests for subtract():
    >>> subtract(4.0, 2.0)
    2.0
    >>> subtract(4, 2)
    2.0
    """
    return float(a - b)


def multiply(a, b):
    """Compute and return the product of two numbers.

    Tests for multiply():
    >>> multiply(4.0, 2.0)
    8.0
    >>> multiply(4, 2)
    8.0
    """
    return float(a * b)


def divide(a, b):
    """Compute and return the quotient of two numbers.

    Tests for divide():
    >>> divide(4.0, 2.0)
    2.0
    >>> divide(4, 2)
    2.0
    >>> divide(4, 0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    return float(a / b)
