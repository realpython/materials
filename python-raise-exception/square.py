def squared(numbers):
    if not isinstance(numbers, list | tuple):
        raise TypeError(
            f"list or tuple expected, got '{type(numbers).__name__}'"
        )
    return [number**2 for number in numbers]
