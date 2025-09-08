employee = ("Jane", "Doe", 31, "Software Developer")
print(employee)
print(type((1)))
print(type((1,)))

# Concatenation
first_tuple = (1, 2)
second_tuple = (3, 4)
third_tuple = first_tuple + second_tuple
print(third_tuple)

# Built-in functions
numbers = (1, 2, 3)
print(len(numbers))
numbers = (1, 2, 3)
print(list(numbers))

# Tuple methods
letters = ("a", "b", "b", "c", "a")
print(letters.count("a"))
print(letters.count("c"))
print(letters.count("d"))
print(letters.index("a"))
print(letters.index("c"))
print(letters.index("d"))

# Indexing and slicing
employee = ("Jane", "Doe", 31, "Software Developer")
print(employee[0])
print(employee[1:3])
