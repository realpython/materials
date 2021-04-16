"""Provide several sample math calculations."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    >>> add(15, 10)
    25
    """
    return a + b


def substract(a: float, b: float) -> float:
    """Return the difference of two numbers.

    >>> substract(15, 10)
    5
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers.

    >>> multiply(15, 10)
    150
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers.

    >>> divide(15, 10)
    1.5

    If ``b`` is zero, then a ZeroDivisionError will be raised.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(base: float, exponent: float = 2) -> float:
    """Return base to the power of exponent.

    >>> power(15, 10)
    576650390625
    """
    return base ** exponent


def sqrt(a: float) -> float:
    """Return the square root of a.

    >>> sqrt(25)
    5

    If a is lower than zero, then a ValueError is raised.
    """
    if a < 0:
        raise ValueError("math domain error")
    return a ** (1 / 2)
