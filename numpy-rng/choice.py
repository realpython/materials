import numpy as np

rng = np.random.default_rng()
input_array_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(rng.choice(input_array_1d, size=3, replace=False))
print(rng.choice(input_array_1d, size=(2, 3), replace=False))
