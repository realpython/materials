import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(seed=2310)
weights = rng.normal(1023, 19, size=5_000)

print(f"Mean of weights: {weights.mean():.2f}g")
print(f"Standard deviation of weights: {weights.std():.2f}g")

plt.hist(weights, bins=50)
plt.show()
