cities = ["Hanoi", "Adelaide", "Odessa", "Vienna"]
separator = "->"

travel_path = ""
for i, city in enumerate(cities):
    travel_path += city
    if i < len(cities) - 1:
        travel_path += separator

print(travel_path)
