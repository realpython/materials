# more_exception_identification.py

from operator import mul, truediv


def calculate(operator, operand1, operand2):
    return operator(operand1, operand2)


try:
    first = float(input("What is your first number? "))
    second = float(input("What is your second number? "))
    operation = input("Enter either * or /: ")
    if operation == "*":
        answer = calculate(mul, first, second)
    elif operation == "/":
        answer = calculate(truediv, first, second)
    else:
        raise RuntimeError(f"'{operation}' is an unsupported operation")   
except (RuntimeError, ValueError, ZeroDivisionError) as err:
    print(f"A {type(err).__name__} has occurred")
    match err:
        case RuntimeError():
            print(f"You have entered an invalid symbol: {err}")
        case ValueError():
            print(f"You have not entered a number: {err}")
        case ZeroDivisionError():
            print(f"You can't divide by zero: {err}")
else:
    print(f"{first} {operation} {second} = {answer}")

