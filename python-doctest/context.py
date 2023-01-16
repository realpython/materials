total = 100


def decrement_by(number):
    """Decrement the global total variable by a given number.

    >>> local_total = decrement_by(50)
    >>> local_total
    50

    Changes to total don't affect the code's global scope
    >>> total
    100
    """
    global total
    total -= number
    return total


def increment_by(number):
    """Increment the global total variable by a given number.

    The initial value of total's shallow copy is 50
    >>> increment_by(10)
    60

    The local_total variable is not defined in this test
    >>> local_total
    Traceback (most recent call last):
    NameError: name 'local_total' is not defined
    """
    global total
    total += number
    return total
