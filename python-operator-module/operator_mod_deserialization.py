import pickle

with open("mod_pickle.pkl", "rb") as f:
    unpickled_modulus = pickle.load(f)

print(unpickled_modulus(7, 4))
