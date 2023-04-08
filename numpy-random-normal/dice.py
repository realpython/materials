import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=2310)

rolls = rng.integers(low=1, high=6, endpoint=True, size=(10_000, 2))
plt.hist(rolls.mean(axis=1), bins=21)
plt.show()

rolls = rng.integers(low=1, high=6, endpoint=True, size=(10_000, 10))
plt.hist(rolls.mean(axis=1), bins=41)
plt.show()
