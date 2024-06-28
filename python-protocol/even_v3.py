from collections.abc import Iterable


def filter_even_numbers(numbers: Iterable[int]) -> list[int]:
    return [number for number in numbers if number % 2 == 0]


print(filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(filter_even_numbers((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(filter_even_numbers({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))
