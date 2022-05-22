"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
- `power(a, b)` - Returns the base to the power of the exponent.
- `sqrt(a)` - Returns the square root of a number.
"""

from typing import Union


def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the artihmetic sum of both operands, `a` and `b`.
    """

    return float(a + b)


def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Calculate the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a: A number representing the minuend in the subtraction.
        b: A number representing the subtrahend in the subtraction.

    Returns:
        A number representing the difference between the two numbers, `a` and `b`.
    """

    return float(a - b)


def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a: A number representing the multiplicand in the multiplication.
        b: A number representing the multiplier in the multiplication.

    Returns:
        A number representing the product of the two numbers, `a` and `b`.
    """

    return float(a * b)


def divide(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the quotient of two numbers.

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0
        >>> divide(4, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero

    Args:
        a: A number representing the dividend in the division.
        b: A number representing the divisor in the division.

    Returns:
        A number representing the quotient of the two numbers, `a` and `b`.

    Raises:
        ZeroDivisionError: An error occurs when the divisor is `0`.
    """

    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)


def power(a: Union[float, int], b: Union[float, int] = 2.0) -> float:
    """Compute and return the base to the power of the exponent.

    Examples:
        >>> power(4.0, 2.0)
        16.0
        >>> power(4, 2)
        16.0
        >>> power(4)
        16.0

    Args:
        a: A number representing the base in the exponentiation.
        b: A number representing the exponent in the exponentiation.

    Returns:
        A number representing the power of the two numbers, `a` and `b`.
    """

    return float(a**b)


def sqrt(a: Union[float, int]) -> float:
    """Compute and return the square root of a number.

    Examples:
        >>> sqrt(4.0)
        2.0
        >>> sqrt(4)
        2.0
        >>> sqrt(-2)
        Traceback (most recent call last):
        ...
        ValueError: math domain error

    Args:
        a: A number representing the radicand of the square root operation.

    Returns:
        A number representing the square root of `a`.

    Raises:
        ValueError: An error occurs when the radicand is below `0`.
    """

    if a < 0:
        raise ValueError("math domain error")
    return float(a ** (1 / 2))
