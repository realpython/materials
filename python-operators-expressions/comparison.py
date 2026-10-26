# Comparing objects of different types for equality
print(2 == "2")

# Non-equality comparisons between different types raise a TypeError
try:
    print(5 < "7")
except TypeError as error:
    print(error)
