# Section: Customizing the Colormap and Style of Your Scatter Plot

import matplotlib.pyplot as plt
import numpy as np

price_orange = np.asarray([2.50, 1.23, 4.02, 3.25, 5.00, 4.40])
sales_per_day_orange = np.asarray([34, 62, 49, 22, 13, 19])
profit_margin_orange = np.asarray([20, 35, 40, 20, 27.5, 15])
sugar_content_orange = [15, 35, 22, 27, 38, 14]

price_cereal = np.asarray([1.50, 2.50, 1.15, 1.95])
sales_per_day_cereal = np.asarray([67, 34, 36, 12])
profit_margin_cereal = np.asarray([20, 42.5, 33.3, 18])
sugar_content_cereal = [21, 49, 29, 24]

plt.scatter(
    x=price_orange,
    y=sales_per_day_orange,
    s=profit_margin_orange * 10,
    c=sugar_content_orange,
    cmap="jet",
    alpha=0.5,
)
plt.scatter(
    x=price_cereal,
    y=sales_per_day_cereal,
    s=profit_margin_cereal * 10,
    c=sugar_content_cereal,
    cmap="jet",
    marker="d",
    alpha=0.5,
)

plt.title("Sales vs Prices for Orange Drinks and Cereal Bars")
plt.legend(["Orange Drinks", "Cereal Bars"])
plt.xlabel("Price (Currency Unit)")
plt.ylabel("Average weekly sales")
plt.text(
    2.7,
    55,
    "Size of marker = profit margin\nColor of marker = sugar content",
)
plt.colorbar()

plt.show()
