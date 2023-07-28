# Deserialize the function unsuccessfully.

import pickle

with open("calculate_modulus.pkl", "rb") as f:
    unpickled_modulus = pickle.load(f)

print(unpickled_modulus(7, 4))
