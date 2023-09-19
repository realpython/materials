from operator import itemgetter

item = ("name", "Guido")

getter = itemgetter(0)
getter(item)  # Returns "name"

getter = itemgetter(1)
getter(item)  # Returns "Guido"


fruit_inventory = [("banana", 5), ("orange", 15), ("apple", 3), ("kiwi", 0)]

# Sort by key
sorted(fruit_inventory, key=itemgetter(0))

# Sort by value
sorted(fruit_inventory, key=itemgetter(1))

# Raises IndexError
# sorted(fruit_inventory, key=itemgetter(2))


people = {3: "Jim", 2: "Jack", 4: "Jane", 1: "Jill"}

sorted(people.items(), key=itemgetter(1))  # Sort by value


scores = {
    "Jack": 14,
    "Jill": 14,
    "John": 15,
    "Jane": 15,
    "Jim": 14,
    "Jess": 14,
}

# Sorts by value, but keeps names in alphabetical order
print(sorted(scores.items(), key=itemgetter(1, 0)))
