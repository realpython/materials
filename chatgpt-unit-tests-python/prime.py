import pytest


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),  # Smallest prime
        (3, True),  # Prime
        (4, False),  # Composite (2*2)
        (5, True),  # Prime
        (11, True),  # Prime
        (12, False),  # Composite (2*6)
        (13, True),  # Prime
        (25, False),  # Composite (5*5)
        (29, True),  # Prime
        (1, False),  # Not prime by definition
        (0, False),  # Not prime
        (-1, False),  # Negative number
        (-11, False),  # Negative number
    ],
)
def test_is_prime(number, expected):
    assert is_prime(number) == expected
