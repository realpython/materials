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
