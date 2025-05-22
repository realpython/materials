def odd_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            yield f"{number} is even"
        else:
            yield f"{number} is odd"


# Example usage
numbers = [2, 2, 3, 11, 4, 5, 7, 4]
for result in odd_even(numbers):
    print(result)
