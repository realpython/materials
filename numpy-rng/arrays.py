import numpy as np

rng = np.random.default_rng()

print(rng.random(size=(5,)))
print(rng.random(size=(5, 3)))
print(rng.random(size=(3, 4, 2)))
