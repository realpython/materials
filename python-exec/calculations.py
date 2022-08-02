# calculations.py


def add(a, b):
    """Return the sum of two numbers.

    Tests:
        >>> add(5, 6)
        11
        >>> add(2.3, 5.4)
        7.7
        >>> add("2", 3)
        Traceback (most recent call last):
        TypeError: numeric type expected for "a" and "b"
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError('numeric type expected for "a" and "b"')
    return a + b


# ...
