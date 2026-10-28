def average(numbers):
    if not numbers:
        raise ValueError("average() requires at least one number")
    return sum(numbers) / len(numbers)


average([1, 2.2, 3])
