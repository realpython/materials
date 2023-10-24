"""Prompt
Write a NumPy-style docstring for the following function.
Add a section with usage examples as doctest tests:

def add(a, b):
    return a + b
"""


# Output:
def add(a, b):
    """
    Add two numbers together.

    This function takes two numbers (either integers or floats)
    as arguments and returns their sum.

    Parameters
    ----------
    a : int or float
        The first number to add.
    b : int or float
        The second number to add.

    Returns
    -------
    int or float
        The sum of the two input numbers.

    Examples
    --------
    >>> add(1, 2)
    3
    >>> add(5.5, 2.5)
    8.0
    >>> add(100, -50)
    50
    """
    return a + b
