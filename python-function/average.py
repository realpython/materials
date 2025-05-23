def cumulative_average(numbers):
    total = 0
    for items, number in enumerate(numbers, 1):
        total += number
        yield total / items


values = [5, 3, 8, 2, 5]  # Simulates a large data set

for cum_average in cumulative_average(values):
    print(f"Cumulative average: {cum_average:.2f}")


def average(*args):
    return sum(args) / len(args)


print(average(1, 2, 3, 4, 5, 6))
print(average(1, 2, 3, 4, 5, 6, 7))
print(average(1, 2, 3, 4, 5, 6, 7, 8))
