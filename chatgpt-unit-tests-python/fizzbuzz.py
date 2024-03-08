def fizzbuzz(number):
    """Solves the FizzBuzz problem.

    Return "fizz" for numbers divisible by 3,
    "buzz" for numbers divisible by 5,
    "fizz buzz" for numbers divisible by both,
    and the number itself otherwise.

    >>> fizzbuzz(3)
    'fizz'
    >>> fizzbuzz(5)
    'buzz'
    >>> fizzbuzz(15)
    'fizz buzz'
    >>> fizzbuzz(4)
    4
    >>> fizzbuzz(30)
    'fizz buzz'
    >>> fizzbuzz(9)
    'fizz'
    >>> fizzbuzz(10)
    'buzz'
    """

    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
