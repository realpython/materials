import pickle


def calculate_modulus(operand1, operand2):
    return operand1 % operand2


print(calculate_modulus(7, 4))


with open("calculate_modulus.pkl", "wb") as f:
    pickle.dump(calculate_modulus, f)

# De-serialize the function.

with open("calculate_modulus.pkl", "rb") as f:
    unpickled_modulus = pickle.load(f)

print(unpickled_modulus(7, 4))
