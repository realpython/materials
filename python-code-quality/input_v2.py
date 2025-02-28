user_input = input("Enter number: ")
try:
    number = int(user_input)
except ValueError:
    print("Error: invalid input")
else:
    print(f"Duplicate: {number * 2}")
