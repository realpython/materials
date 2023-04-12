import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

rng = np.random.default_rng(seed=2310)
numbers = rng.normal(size=10_000)

print(f"Mean of numbers: {numbers.mean():.3f}")
print(f"Standard deviation of numbers: {numbers.std():.3f}")

bins = 100
bin_width = (numbers.max() - numbers.min()) / bins
hist_area = len(numbers) * bin_width

plt.hist(numbers, bins=bins)
plt.show()

x = np.linspace(-4, 4, 101)
plt.plot(x, scipy.stats.norm.pdf(x))
plt.show()

x = np.linspace(numbers.min(), numbers.max(), 101)
plt.hist(numbers, bins=bins)
plt.plot(x, scipy.stats.norm.pdf(x) * hist_area)
plt.show()
