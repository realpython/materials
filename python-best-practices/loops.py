# Avoid this:
# items = ["apple", "banana", "cherry"]
# labeled = []
# i = 0
# while i < len(items):
#     labeled.append(f"{i}: {items[i].upper()}")
#     i += 1


# Favor this:
items = ["apple", "banana", "cherry"]
labeled = []
for index, item in enumerate(items):
    labeled.append(f"{index}: {item.upper()}")
