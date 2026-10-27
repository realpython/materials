import random
import statistics


def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = statistics.median(
            [
                numbers[0],
                numbers[len(numbers) // 2],
                numbers[-1],
            ]
        )
        items_less, pivot_items, items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot],
        )

        return quicksort(items_less) + pivot_items + quicksort(items_greater)


def get_random_numbers(length, minimum=1, maximum=100):
    numbers = []
    for _ in range(length):
        numbers.append(random.randint(minimum, maximum))

    return numbers


if __name__ == "__main__":
    print(quicksort([]))
    print(quicksort([42]))
    print(quicksort([5, 2, 6, 3]))
    print(quicksort([10, -3, 21, 6, -8]))

    numbers = get_random_numbers(20)
    print(numbers)
    print(quicksort(numbers))
