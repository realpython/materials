import numpy as np

rng = np.random.default_rng()

scalar = rng.poisson(lam=5)
print(scalar)

sample_1d_array = rng.poisson(lam=5, size=4)
print(sample_1d_array)

sample_2d_array = rng.poisson(lam=5, size=(2, 3))
print(sample_2d_array)
