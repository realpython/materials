name = "Pythonista"
day = "Friday"  # Of course 😃

print("Hello, {}! Today is {}.".format(name, day))


numbers = {"one": 1, "two": 2, "three": 3}
print("{one}-{two}-{three}".format(**numbers))
print("{one}-{two}".format(**numbers))
