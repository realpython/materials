from collections import Counter


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


def mean(data):
    return sum(data) / len(data)


def median(data):
    n = len(data)
    index = n // 2
    if n % 2:
        return sorted(data)[index]
    return sum(sorted(data)[index - 1 : index + 1]) / 2


def mode(data):
    c = Counter(data)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
