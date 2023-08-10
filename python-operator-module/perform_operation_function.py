from operator import add, mul, sub, truediv


def perform_operation(operator_function, operand1, operand2):
    return operator_function(operand1, operand2)


number1 = 10
number2 = 5

calculations = [add, sub, mul, truediv]

for op_function in calculations:
    print(perform_operation(op_function, number1, number2))
