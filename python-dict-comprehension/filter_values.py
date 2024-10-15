numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
print({key: value for key, value in numbers.items() if value % 2 == 0})
