# Avoid this:
# def add(a, b):
#     """Return the sum of a and b."""
#     return a + b


# Favor this:
def add(a, b):
    """Sum two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b
