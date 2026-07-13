# Sections: Getting Started With plt.scatter() / Comparing plt.scatter() and plt.plot()

import matplotlib.pyplot as plt

price = [2.50, 1.23, 4.02, 3.25, 5.00, 4.40]
sales_per_day = [34, 62, 49, 22, 13, 19]

plt.scatter(price, sales_per_day)
# plt.plot(price, sales_per_day, "o")  # equivalent using plt.plot()
plt.show()
