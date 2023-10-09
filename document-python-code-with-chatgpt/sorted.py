"""Prompt
Write a Google-style docstring for a function with the following signature:

sorted(iterable, key=None, reverse=False):
"""


# Output:
def sorted(iterable, key=None, reverse=False):
    """
    Sorts objects from the provided iterable in ascending order
    by default, descending order if 'reverse' is True.

    Args:
        iterable (iterable): Iterable of comparable objects that
        are to be sorted.

        key (Callable, optional): Specifies a function to extract
        a comparison key from each element.
        The iterable objects are sorted based on the keys extracted.
        By default, the elements themselves are compared.

        reverse (bool, optional): If set to True, then the list
        elements are sorted in descending order.
        Default is False.

    Returns:
        list: A new sorted list from the items in the iterable.
    """
