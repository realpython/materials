import pickle

with open("operators.pkl", mode="rb") as f:
    operators = pickle.load(f)


def perform_operation(op_string, number1, number2):
    return operators[op_string](number1, number2)


print(perform_operation("*", 10, 5))
