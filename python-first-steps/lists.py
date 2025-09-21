# Define an empty list
empty = []
print(empty)
# Define a list of numbers
numbers = [1, 2, 3, 100]
print(numbers)
# Modify the list in place
numbers[3] = 200
print(numbers)
# Define a list of strings
print(["batman", "superman", "spiderman"])
# Define a list of objects with different data types
print(["Hello World", [4, 5, 6], False])

# Indexing
numbers = [1, 2, 3, 4]
print(numbers[0])
print(numbers[1])
superheroes = ["batman", "superman", "spiderman"]
print(superheroes[-1])
print(superheroes[-2])

# Slicing
numbers = [1, 2, 3, 4]
new_list = numbers[0:3]
print(new_list)

# Nested lists
mixed_types = ["Hello World", [4, 5, 6], False]
print(mixed_types[0][6])
print(mixed_types[1][2])

# Concatenation
fruits = ["apples", "grapes", "oranges"]
veggies = ["corn", "kale", "spinach"]
print(fruits + veggies)

# Built-in functions
numbers = [1, 2, 3, 4]
print(len(numbers))

# List methods
fruits = ["apples", "grapes", "oranges"]
fruits.append("blueberries")
print(fruits)
fruits.sort()
print(fruits)
numbers = [1, 2, 3, 4]
numbers.pop(2)
print(numbers)
