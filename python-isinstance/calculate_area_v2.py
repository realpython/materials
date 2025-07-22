def calculate_area(length, breadth):
    if isinstance(length, int) and isinstance(breadth, int):
        return length * breadth
    raise TypeError("Both arguments must be integers")


print(f"{calculate_area(5, 3) = }")
print(f"{calculate_area(5, "3") = }")
print(f"{calculate_area("5", "3") = }")
