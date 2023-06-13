class MathLibraryError(Exception):
    pass


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as error:
        raise MathLibraryError(error)
