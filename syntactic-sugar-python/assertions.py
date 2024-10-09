number = 42
if __debug__:
    if not number > 0:
        raise AssertionError("number must be positive")

number = -42
if __debug__:
    if not number > 0:
        raise AssertionError("number must be positive")
