numbers = {"one": 1, "two": 2, "thee": 3, "four": 4}

for key, value in reversed(numbers.items()):
    print(key, "->", value)
