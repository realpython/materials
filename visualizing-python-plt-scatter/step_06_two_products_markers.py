# Section: Changing the Shape

import matplotlib.pyplot as plt
import numpy as np

low = (0, 1, 0)
medium = (1, 1, 0)
high = (1, 0, 0)

price_orange = np.asarray([2.50, 1.23, 4.02, 3.25, 5.00, 4.40])
sales_per_day_orange = np.asarray([34, 62, 49, 22, 13, 19])
profit_margin_orange = np.asarray([20, 35, 40, 20, 27.5, 15])
sugar_content_orange = [low, high, medium, medium, high, low]

price_cereal = np.asarray([1.50, 2.50, 1.15, 1.95])
sales_per_day_cereal = np.asarray([67, 34, 36, 12])
profit_margin_cereal = np.asarray([20, 42.5, 33.3, 18])
sugar_content_cereal = [low, high, medium, low]

plt.scatter(
    x=price_orange,
    y=sales_per_day_orange,
    s=profit_margin_orange * 10,
    c=sugar_content_orange,
)
plt.scatter(
    x=price_cereal,
    y=sales_per_day_cereal,
    s=profit_margin_cereal * 10,
    c=sugar_content_cereal,
    marker="d",
)
plt.show()
