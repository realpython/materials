# def sum_even_numbers(numbers):
#     even_numbers = [number for number in numbers if number % 2 == 0]
#     return sum(even_numbers)


def sum_even_numbers(numbers):
    return sum(number for number in numbers if number % 2 == 0)


sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
