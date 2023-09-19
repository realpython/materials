import numpy as np

rng = np.random.default_rng()
matrix = rng.random(size=(5000, 5000))
matrix @ matrix
