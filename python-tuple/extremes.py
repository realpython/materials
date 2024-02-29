def find_extremes(iterable):
    data = tuple(iterable)
    if len(data) == 0:
        raise ValueError("input iterable must not be empty")
    return min(data), max(data)
