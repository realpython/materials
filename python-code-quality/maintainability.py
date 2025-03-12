def process(numbers):
    cleaned = [number for number in numbers if number >= 0]
    return sum(cleaned)


print(process([1, 2, 3, -1, -2, -3]))


def clean_data(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number >= 0]


def calculate_total(numbers: list[int]) -> int:
    return sum(numbers)


cleaned = clean_data([1, 2, 3, -1, -2, -3])
print(calculate_total(cleaned))
