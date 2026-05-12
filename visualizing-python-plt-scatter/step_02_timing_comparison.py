# Section: Comparing plt.scatter() and plt.plot()

import timeit
import matplotlib.pyplot as plt  # noqa: F401

price = [2.50, 1.23, 4.02, 3.25, 5.00, 4.40]
sales_per_day = [34, 62, 49, 22, 13, 19]

print(
    "plt.scatter()",
    timeit.timeit(
        "plt.scatter(price, sales_per_day)",
        number=1000,
        globals=globals(),
    ),
)
print(
    "plt.plot()",
    timeit.timeit(
        "plt.plot(price, sales_per_day, 'o')",
        number=1000,
        globals=globals(),
    ),
)
