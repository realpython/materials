# Use single quotes
print("Hello there!")
# Use double quotes
print("Welcome to Real Python!")
# Use triple quotes
print("""Thanks for joining us!""")
# Escape characters
print("I can't believe it!")
print("can't")

# Concatenation
print("Happy" + " " + "pythoning!")

# Built-in functions
print(len("Happy pythoning!"))

# String methods
print(" ".join(["Happy", "pythoning!"]))
print("Happy pythoning!".upper())
print("HAPPY PYTHONING!".lower())
name = "John Doe"
age = 25
print("My name is {0} and I'm {1} years old".format(name, age))

# f-strings
print(f"My name is {name} and I'm {age} years old")

# Indexing
welcome = "Welcome to Real Python!"
print(welcome[0])
print(welcome[11])
print(welcome[-1])

# Slicing
print(welcome[0:7])
print(welcome[11:22])
