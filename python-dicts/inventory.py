inventory = {"apple": 100, "orange": 80, "banana": 100}
inventory.get("apple")

print(inventory.get("mango"))

print(inventory.get("mango", 0))

print(inventory.values())

print(inventory.keys())

print(inventory.items())
