import pickle
import operator

print(operator.mod(7, 4))


with open("mod_pickle.pkl", "wb") as f:
    pickle.dump(operator.mod, f)
