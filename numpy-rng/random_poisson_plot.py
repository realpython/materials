import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng()
samples = rng.poisson(lam=5, size=10_000)
values, frequency = np.unique(samples, return_counts=True)

plt.title("Random Poisson Distribution.")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.plot(values, frequency, "ro")
plt.show()
