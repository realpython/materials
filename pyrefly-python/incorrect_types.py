def average(numbers: list[int | float]) -> float:
    if not numbers:
        raise ValueError("average() requires at least one number")
    return sum(numbers) / len(numbers)


average(["a", "b", "c"])
average(["d", "e", "f"])
