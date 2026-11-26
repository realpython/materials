# Avoid this:
# def add(a, b):
#     return a + b


# import random


# def test_add():
#     a = random.randint(50, 150)
#     b = random.randint(50, 150)
#     result = add(a, b)
#     assert 50 <= result <= 300
#     print("OK")


# Favor this:
# import pytest
# from calculations import add


# @pytest.mark.parametrize(
#     "a, b, expected",
#     [
#         (100, 10, 110),
#         (100, 35, 135),
#         (200, -50, 150),
#     ],
# )
# def test_add(a, b, expected):
#     assert add(a, b) == expected
