# Section: Changing the Color

import matplotlib.pyplot as plt
import numpy as np

price = np.asarray([2.50, 1.23, 4.02, 3.25, 5.00, 4.40])
sales_per_day = np.asarray([34, 62, 49, 22, 13, 19])
profit_margin = np.asarray([20, 35, 40, 20, 27.5, 15])

low = (0, 1, 0)
medium = (1, 1, 0)
high = (1, 0, 0)

sugar_content = [low, high, medium, medium, high, low]

plt.scatter(
    x=price,
    y=sales_per_day,
    s=profit_margin * 10,
    c=sugar_content,
)
plt.show()
