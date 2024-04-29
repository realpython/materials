import pytest


def in_interval(number: int, start: int, end: int) -> bool:
    return start <= number <= end


@pytest.mark.parametrize(
    "number, start, end, expected",
    [
        (5, 1, 10, True),  # Test case inside the interval
        (1, 1, 10, True),  # Edge case: number equals start
        (10, 1, 10, True),  # Edge case: number equals end
        (0, 1, 10, False),  # Number below the interval
        (11, 1, 10, False),  # Number above the interval
        (5, 5, 5, True),  # Edge case: start equals end equals number
        (-1, -5, 5, True),  # Test case with negative numbers
        (-6, -5, 5, False),  # Number below the interval with negatives
    ],
)
def test_in_interval(number, start, end, expected):
    assert in_interval(number, start, end) == expected
