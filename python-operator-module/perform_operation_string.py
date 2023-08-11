def perform_operation(operator_string, operand1, operand2):
    if operator_string == "+":
        return operand1 + operand2
    elif operator_string == "-":
        return operand1 - operand2
    elif operator_string == "*":
        return operand1 * operand2
    elif operator_string == "/":
        return operand1 / operand2
    else:
        return "Invalid operator."


number1 = 10
number2 = 5

calculations = ["+", "-", "*", "/"]

for op_string in calculations:
    print(perform_operation(op_string, number1, number2))
