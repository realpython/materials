__all__ = []
if len(__all__) == 0:
    raise ImportError("wildcard import not allowed")


def add(a, b):
    return float(a + b)


def subtract(a, b):
    return float(a - b)


def multiply(a, b):
    return float(a * b)


def divide(a, b):
    return float(a / b)
