print("%d" % 123.123)  # As an integer
print("%o" % 42)  # As an octal
print("%x" % 42)  # As a hex
print("%e" % 1234567890)  # In scientific notation
print("%f" % 42)  # As a floating-point number


# Named replacement fields
jane = {"first_name": "Jane", "last_name": "Doe"}
print("Full name: %(first_name)s %(last_name)s" % jane)
# Minimal width of 15 chars
print("%-15f" % 3.1416)  # Aligned to the left
print("%15f" % 3.1416)  # Aligned to the right
# Dynamic width
width = 15
print("%-*f" % (width, 3.1416))
print("%*f" % (width, 3.1416))
# Precision
print("%.2f" % 3.141592653589793)
print("%.4f" % 3.141592653589793)
print("%.8f" % 3.141592653589793)


print("%o" % 10)
print("%#o" % 10)
print("%x" % 31)
print("%#x" % 31)

print("%05d" % 42)
print("%10d" % 42)
print("%-10d" % 42)
print("% d" % 42)
print("% d" % -42)
print("%+d" % 42)
print("%+d" % -42)
