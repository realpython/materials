# Section: Further Scatter Plot Techniques With plt.scatter()

import random
import matplotlib.pyplot as plt
import numpy as np

n_buses = 40
bus_times = np.asarray([random.randint(0, 59) for _ in range(n_buses)])
bus_likelihood = np.asarray([random.random() for _ in range(n_buses)])

plt.scatter(x=bus_times, y=bus_likelihood)
plt.title("Randomly chosen bus arrival times and relative probabilities")
plt.ylabel("Relative probability of bus arrivals")
plt.xlabel("Minutes past the hour")
plt.show()
