fruits = {"apple": 0.40, "orange": 0.35, "banana": 0.25}

for fruit in fruits.copy():
    if fruits[fruit] >= 0.30:
        del fruits[fruit]
