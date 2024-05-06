def validate(value):
    if not isinstance(value, int | float) or value <= 0:
        raise ValueError("positive number expected")
    return value
