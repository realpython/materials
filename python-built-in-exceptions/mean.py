def mean(grades):
    try:
        return sum(grades) / len(grades)
    except ZeroDivisionError:
        raise ValueError("mean() arg shouldn't be empty") from None
