# import pytest

# def greet(name):
#     print(f"Hello, {name}!")


# def test_greet(capsys):
#     greet("Alice")
#     captured = capsys.readouterr()
#     assert captured.out.strip() == "Hello, Alice!"


def greet(name: str) -> str:
    return f"Hello, {name}!"


# Easy to test
def test_greet():
    assert greet("Alice") == "Hello, Alice!"
