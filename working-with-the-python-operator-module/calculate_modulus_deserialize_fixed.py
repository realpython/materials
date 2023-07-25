# De-serialize the function successfully.

import pickle


def calculate_modulus(operand1, operand2):
    return operand1 % operand2


with open("calculate_modulus.pkl", "rb") as f:
    unpickled_modulus = pickle.load(f)

print(unpickled_modulus(7, 4))
