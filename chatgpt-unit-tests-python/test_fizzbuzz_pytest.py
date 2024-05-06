import pytest
from fizzbuzz import fizzbuzz

# def test_fizzbuzz_with_number_divisible_by_15():
#     assert fizzbuzz(30) == "fizz buzz"


# def test_fizzbuzz_with_number_divisible_by_3():
#     assert fizzbuzz(9) == "fizz"


# def test_fizzbuzz_with_number_divisible_by_5():
#     assert fizzbuzz(10) == "buzz"


# def test_fizzbuzz_with_number_not_divisible_by_3_or_5():
#     assert fizzbuzz(4) == 4


# def test_fizzbuzz_with_zero():
#     assert fizzbuzz(0) == "fizz buzz"


@pytest.mark.parametrize(
    "input,expected",
    [
        (30, "fizz buzz"),  # Divisible by 15
        (9, "fizz"),  # Divisible by 3
        (10, "buzz"),  # Divisible by 5
        (4, 4),  # Not divisible by 3 or 5
        (0, "fizz buzz"),  # Edge case: 0 (divisible by 15)
        (33, "fizz"),  # Additional case: Divisible by 3
        (55, "buzz"),  # Additional case: Divisible by 5
        (98, 98),  # Additional case: Not divisible by 3 or 5
    ],
)
def test_fizzbuzz(input, expected):
    assert (
        fizzbuzz(input) == expected
    ), f"Expected {expected} for input {input}"
