# exception_identification.py

try:
    first = float(input("What is your first number? "))
    second = float(input("What is your second number? "))
    print(f"{first} divided by {second} is {first / second}")
except (ValueError, ZeroDivisionError): as err:
    print(f"A {type(err).__name__} has occurred.")
