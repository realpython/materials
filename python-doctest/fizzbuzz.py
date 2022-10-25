# The commented versions of fizzbuzz() below reflect the steps
# followed to get to the final version at the end of the file.

# Replace numbers that are divisible by 3 with "fizz"
# def fizzbuzz(numbers):
#     """Implement the Fizz buzz game.

#     >>> fizzbuzz([3, 6, 9, 12])
#     ['fizz', 'fizz', 'fizz', 'fizz']
#     """


# # Replace numbers that are divisible by 3 with "fizz"
# def fizzbuzz(numbers):
#     """Implement the Fizz buzz game.

#     >>> fizzbuzz([3, 6, 9, 12])
#     ['fizz', 'fizz', 'fizz', 'fizz']
#     """
#     result = []
#     for number in numbers:
#         if number % 3 == 0:
#             result.append("fizz")
#         else:
#             result.append(number)
#     return result


# Replace numbers that are divisible by 5 with "buzz"
# def fizzbuzz(numbers):
#     """Implement the Fizz buzz game.

#     >>> fizzbuzz([3, 6, 9, 12])
#     ['fizz', 'fizz', 'fizz', 'fizz']

#     >>> fizzbuzz([5, 10, 20, 25])
#     ['buzz', 'buzz', 'buzz', 'buzz']
#     """
#     result = []
#     for number in numbers:
#         if number % 3 == 0:
#             result.append("fizz")
#         elif number % 5 == 0:
#             result.append("buzz")
#         else:
#             result.append(number)
#     return result


# Replace numbers that are divisible by 3 and 5 with "fizz buzz"
def fizzbuzz(numbers):
    """Implement the Fizz buzz game.

    >>> fizzbuzz([3, 6, 9, 12])
    ['fizz', 'fizz', 'fizz', 'fizz']

    >>> fizzbuzz([5, 10, 20, 25])
    ['buzz', 'buzz', 'buzz', 'buzz']

    >>> fizzbuzz([15, 30, 45])
    ['fizz buzz', 'fizz buzz', 'fizz buzz']

    >>> fizzbuzz([3, 6, 5, 10, 15, 30])
    ['fizz', 'fizz', 'buzz', 'buzz', 'fizz buzz', 'fizz buzz']
    """
    result = []
    for number in numbers:
        if number % 15 == 0:
            result.append("fizz buzz")
        elif number % 3 == 0:
            result.append("fizz")
        elif number % 5 == 0:
            result.append("buzz")
        else:
            result.append(number)
    return result
