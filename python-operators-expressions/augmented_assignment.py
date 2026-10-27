total = 10
total = total + 5
print(total)

# Accumulating into an undefined variable raises a NameError
try:
    count = count + 1
except NameError as error:
    print(error)

# The augmented addition operator does the same job
total = 10
total += 5
print(total)
