blt_sandwich = [
    ["bread", "lettuce", "tomato", "bacon"],
    ["bread", "bacon", "lettuce", "tomato"],
    ["bacon", "bacon", "tomato", "lettuce"],
]
target = "bacon"
found = False
for layer in blt_sandwich:
    for ingredient in layer:
        if ingredient != target:
            print("This is not bacon. Skipping...")
            continue
        print(f"Found the crispy {target}!")
        found = True
        break

    if found:
        print("Enjoying the crunch and worth it.")
        break
