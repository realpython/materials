import pytest

from fizzbuzz import fizzbuzz

# def test_fizzbuzz_with_multiples_of_three():
#     assert fizzbuzz(3) == "fizz"
#     assert fizzbuzz(6) == "fizz"
#     assert fizzbuzz(9) == "fizz"


# def test_fizzbuzz_with_multiples_of_five():
#     assert fizzbuzz(5) == "buzz"
#     assert fizzbuzz(10) == "buzz"
#     assert fizzbuzz(20) == "buzz"


# def test_fizzbuzz_with_multiples_of_fifteen():
#     assert fizzbuzz(15) == "fizz buzz"
#     assert fizzbuzz(30) == "fizz buzz"
#     assert fizzbuzz(45) == "fizz buzz"


# def test_fizzbuzz_with_non_multiples_of_three_or_five():
#     assert fizzbuzz(1) == 1
#     assert fizzbuzz(2) == 2
#     assert fizzbuzz(4) == 4
#     assert fizzbuzz(7) == 7


@pytest.mark.parametrize(
    "number, expected",
    [
        (3, "fizz"),
        (6, "fizz"),
        (9, "fizz"),
        (5, "buzz"),
        (10, "buzz"),
        (20, "buzz"),
        (15, "fizz buzz"),
        (30, "fizz buzz"),
        (45, "fizz buzz"),
        (1, 1),
        (2, 2),
        (4, 4),
        (7, 7),
    ],
)
def test_fizzbuzz(number, expected):
    assert fizzbuzz(number) == expected
