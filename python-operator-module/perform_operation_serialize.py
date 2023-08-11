import operator
import pickle

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

with open("operators.pkl", mode="wb") as f:
    pickle.dump(operators, f)


def perform_operation(op_string, number1, number2):
    return operators[op_string](number1, number2)


print(perform_operation("-", 10, 5))
