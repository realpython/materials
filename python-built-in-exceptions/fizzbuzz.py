# def fizzbuzz(number):
#     if number % 3 == 0:
#         return "fizz"
#     elif number % 5 == 0:
#         return "buzz"
#     elif number % 15 == 0:
#         return "fizz buzz"
#     else:
#         return number


def fizzbuzz(number):
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number


if __name__ == "__main__":
    assert fizzbuzz(9) == "fizz"
    assert fizzbuzz(10) == "buzz"
    assert fizzbuzz(15) == "fizz buzz"
    assert fizzbuzz(7) == 7
    print("All tests pass")
