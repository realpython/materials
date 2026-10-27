from collections.abc import Collection


# A Collection is any object that has a length and can be iterated over
def average(numbers: Collection[int | float]) -> float:
    if not numbers:
        raise ValueError("average() requires at least one number")
    return sum(numbers) / len(numbers)


average([1, 2.2, 3])
average({1, 2.2, 3})
average((1, 2.2, 3))
