def double(numbers):
    for i, _ in enumerate(numbers):
        numbers[i] *= 2


numbers = [1, 2, 3, 4, 5]
print(double(numbers))
