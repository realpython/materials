# exception_identification.py

try:
    first = float(input("What is your first number? "))
    second = float(input("What is your second number? "))
    print(f"{first} divided by {second} is {first / second}")
except (ValueError, ZeroDivisionError) as error:
    print(f"A {type(error).__name__} has occurred.")
