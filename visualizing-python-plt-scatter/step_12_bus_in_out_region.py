# Section: Further Scatter Plot Techniques With plt.scatter()

import random
import matplotlib.pyplot as plt
import numpy as np

mean = 15, 45
sd = 5, 7

x = np.linspace(0, 59, 60)
first_distribution = np.exp(-0.5 * ((x - mean[0]) / sd[0]) ** 2)
second_distribution = 0.9 * np.exp(-0.5 * ((x - mean[1]) / sd[1]) ** 2)
y = first_distribution + second_distribution
y = y / max(y)

n_buses = 40
bus_times = np.asarray([random.randint(0, 59) for _ in range(n_buses)])
bus_likelihood = np.asarray([random.random() for _ in range(n_buses)])

in_region = bus_likelihood < y[bus_times]
out_region = bus_likelihood >= y[bus_times]

plt.scatter(
    x=bus_times[in_region],
    y=bus_likelihood[in_region],
    color="green",
)
plt.scatter(
    x=bus_times[out_region],
    y=bus_likelihood[out_region],
    color="red",
    marker="x",
)

plt.plot(x, y)
plt.title("Randomly chosen bus arrival times and relative probabilities")
plt.ylabel("Relative probability of bus arrivals")
plt.xlabel("Minutes past the hour")
plt.show()
