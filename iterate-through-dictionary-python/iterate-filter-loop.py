numbers = {"one": 1, "two": 2, "three": 3, "four": 4}
small_numbers = {}

for key, value in numbers.items():
    if value <= 2:
        small_numbers[key] = value
