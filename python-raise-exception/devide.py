def divide(x, y):
    for arg in (x, y):
        if not isinstance(arg, int | float):
            raise TypeError(f"number expected, got {type(arg).__name__}")
    if y == 0:
        raise ValueError("denominator can't be zero")
    return x / y


try:
    divide(42, 0)
except Exception as error:
    raise ValueError("invalid argument") from error
