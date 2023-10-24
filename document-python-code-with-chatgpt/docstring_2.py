"""Propmt
Write a Google-style docstring for the following function:

def add(a, b):
    return a + b
"""


# Output:
def add(a, b):
    """Sum two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b


"""Prompt
Write a Numpy-style docstring for the following function:

def add(a, b):
    return a + b
"""


# Output:
def add_(a, b):
    """
    Sum two numbers.

    Parameters
    ----------
    a : int or float
        The first number to be added.
    b : int or float
        The second number to be added.

    Returns
    -------
    int or float
        The sum of a and b.
    """
    return a + b


"""Prompt
Write a Sphinx-style docstring for the following function:

def add(a, b):
    return a + b
"""


# Output:
def add__(a, b):
    """
    Calculate the sum of two numbers.

    :param a: The first number.
    :type a: int or float
    :param b: The second number.
    :type b: int or float
    :return: The sum of the two numbers.
    :rtype: int or float
    """
    return a + b
