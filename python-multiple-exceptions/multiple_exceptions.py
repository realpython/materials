try:
    first = float(input("What is your first number? "))
    second = float(input("What is your second number? "))
    print(f"{first} divided by {second} is {first / second}")
except (ZeroDivisionError, ValueError):
    print("There was an error")
