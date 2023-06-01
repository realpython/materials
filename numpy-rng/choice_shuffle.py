import numpy as np

input_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

rng = np.random.default_rng()
print(rng.choice(input_array, size=2))
print(rng.choice(input_array, size=2, axis=1))
print(rng.choice(input_array, size=3, replace=False))

rng = np.random.default_rng(seed=100)
print(rng.choice(input_array, size=3, replace=False, shuffle=False))

rng = np.random.default_rng(seed=100)
print(rng.choice(input_array, size=3, replace=False, shuffle=True))

rng = np.random.default_rng(seed=100)
print(rng.choice(input_array, size=3, replace=True, shuffle=False))

rng = np.random.default_rng(seed=100)
print(rng.choice(input_array, size=3, replace=True, shuffle=True))
