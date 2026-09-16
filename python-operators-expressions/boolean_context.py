# Numeric values: zero is falsy, everything else is truthy
print(bool(0), bool(0.0), bool(0.0 + 0j))
print(bool(-3), bool(3.14159), bool(1.0 + 1j))

# Strings: the empty string is falsy
print(bool(""))
print(bool(" "))
print(bool("Hello"))

# Containers: empty containers are falsy
print(bool([]))
print(bool([1, 2, 3]))

print(bool(()))
print(bool(("John", 25, "Python Dev")))

print(bool(set()))
print(bool({"square", "circle", "triangle"}))

print(bool({}))
print(bool({"name": "John", "age": 25, "job": "Python Dev"}))
