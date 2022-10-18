def get_even_numbers(numbers):
    """Return the even numbers in a list.

    >>> args = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    >>> expected = [[2, 4], [6, 8], [10, 12]]

    >>> for arg, expected in zip(args, expected):
    ...     get_even_numbers(arg) == expected
    True
    True
    True
    """
    return [number for number in numbers if number % 2 == 0]
