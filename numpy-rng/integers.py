import numpy as np

rng = np.random.default_rng()

for i in range(5):
    print(rng.integers(3))

for count in range(5):
    print(rng.integers(low=1, high=4))

for count in range(5):
    print(rng.integers(low=7))

for count in range(5):
    print(rng.integers(low=1, high=4, endpoint=True))

for count in range(5):
    print(rng.integers(low=7, endpoint=True))
