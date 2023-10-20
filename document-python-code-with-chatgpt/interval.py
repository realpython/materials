"""Prompt
Write a Google-style docstring for a function with the following signature:

def in_interval(number, start, end):
"""


# Output:
def in_interval(number, start, end):
    """
    Checks if a given number is within a specified interval.

    This function takes three arguments: a number, and the start
    and end points of an interval.
    It checks whether the given number falls within the specified
    interval or not.

    Args:
        number (int or float): The number to check.
        start (int or float): The starting point of the interval.
        end (int or float): The ending point of the interval.

    Returns:
        bool: True if the given number falls within the interval,
        False otherwise.

    Raises:
        ValueError: If the start is larger than the end, or if
        the number, start, or end are not numbers.
    """
