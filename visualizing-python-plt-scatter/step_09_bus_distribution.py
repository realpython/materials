# Section: Further Scatter Plot Techniques With plt.scatter()

import matplotlib.pyplot as plt
import numpy as np

mean = 15, 45
sd = 5, 7

x = np.linspace(0, 59, 60)  # Represents each minute within the hour
first_distribution = np.exp(-0.5 * ((x - mean[0]) / sd[0]) ** 2)
second_distribution = 0.9 * np.exp(-0.5 * ((x - mean[1]) / sd[1]) ** 2)
y = first_distribution + second_distribution
y = y / max(y)

plt.plot(x, y)
plt.ylabel("Relative probability of bus arrivals")
plt.xlabel("Minutes past the hour")
plt.show()
