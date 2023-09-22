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
except (RuntimeError, ValueError, ZeroDivisionError) as error:
    print(f"A {type(error).__name__} has occurred")
    match error:
        case RuntimeError():
            print(f"You have entered an invalid symbol: {error}")
        case ValueError():
            print(f"You have not entered a number: {error}")
        case ZeroDivisionError():
            print(f"You can't divide by zero: {error}")
else:
    print(f"{first} {operation} {second} = {answer}")
