def calculate_area(length, breadth):
    if isinstance(length, int) and isinstance(breadth, int):
        return length * breadth
    return "Invalid argument"


calculate_area(5, 3)
calculate_area(5, "3")
calculate_area("5", "3")
