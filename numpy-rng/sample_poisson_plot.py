import matplotlib.pyplot as plt
import numpy as np
from scipy.special import factorial

lam = 4
k_values = np.arange(0, 30)
probabilities = np.power(lam, k_values) * np.exp(-lam) / factorial(k_values)

plt.plot(k_values, probabilities, "ro")
plt.title("Sample Poisson Distribution.")
plt.xlabel("k")
plt.ylabel("P(k)")
plt.show()
