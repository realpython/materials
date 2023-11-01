"""Prompt
Write a Google-style docstring for a function that takes an
integer as an argument and determines whether it’s a prime
number.
"""


# Output:
def is_prime_number(n):
    """
    Determines if an input integer is a prime number.

    This function takes an integer as an argument and checks
    whether it is a prime number. A prime number is a
    positive natural number greater than 1 that has no positive
    integer divisors other than 1 and itself.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if the input integer is a prime number,
        False otherwise.

    Raises:
        ValueError: If n is less than or equal to 1.
    """
