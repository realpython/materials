import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

x = np.linspace(-4, 4, 201)
y = scipy.stats.norm.pdf(x)

fig, ax = plt.subplots()

ax.fill_between(x, y, 0, alpha=0.2, color="green")
ax.fill_between(x[75:126], y[75:126], 0, alpha=1, color="green")
ax.plot(x, y, "k")
ax.plot([-1, -1], [0, y[75]], "k--")
ax.plot([1, 1], [0, y[125]], "k--")
ax.annotate(
    "68%",
    xy=(0.1, 0.25),
    xytext=(2, 0.3),
    arrowprops=dict(facecolor="black", shrink=0.005),
)
ax.set_yticks([])

plt.show()
