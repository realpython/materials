import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

lam = 4
k_values = np.arange(0, 30)
probabil = np.exp(-lam) * np.power(lam, k_values) / factorial(k_values)

plt.plot(k_values, probabil, "ro")
plt.title("Sample Poisson Distribution.")
plt.xlabel("k")
plt.ylabel("P(k)")
plt.show()
