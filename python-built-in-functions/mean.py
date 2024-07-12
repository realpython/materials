def mean(values):
    try:
        return sum(values) / len(values)
    except ZeroDivisionError:
        raise ValueError("mean() arg shouldn't be empty") from None
