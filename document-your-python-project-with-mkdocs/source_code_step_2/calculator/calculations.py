def add(a, b):
    return float(a + b)


def subtract(a, b):
    return float(a - b)


def multiply(a, b):
    return float(a * b)


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
