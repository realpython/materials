"""Control how reshape() rearranges data with the order parameter."""

import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Row-major (C) order fills each row before moving to the next
print('order="C":')
print(numbers.reshape((2, 4), order="C"))

# Column-major (F) order fills each column before moving to the next
print('order="F":')
print(numbers.reshape((2, 4), order="F"))
