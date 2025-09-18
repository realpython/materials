print({"John", "Jane", "Linda"})
print(set(["David", "Mark", "Marie"]))
empty = set()
print(empty)

# Unique elements
print(set([1, 2, 2, 3, 4, 5, 3]))

# Built-in functions
employees = {"John", "Jane", "Linda"}
print(len(employees))

# Set operations
primes = {2, 3, 5, 7}
evens = {2, 4, 6, 8}
print(primes | evens)  # Union
print(primes & evens)  # Intersection
print(primes - evens)  # Difference

# Set methods
primes = {2, 3, 5, 7}
primes.add(11)
print(primes)
primes.remove(11)
print(primes)
