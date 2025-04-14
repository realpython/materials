pet_animals = {"dog", "cat", "hamster", "parrot"}
farm_animals = {"cow", "chicken", "goat", "dog", "cat"}

print(pet_animals | farm_animals)
print(pet_animals.union(farm_animals))

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
a.union(b, c, d)
print(a | b | c | d)
