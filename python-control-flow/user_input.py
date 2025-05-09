user_input = input("Enter an integer number: ")

try:
    number = int(user_input)
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"Success: you entered {number}")
