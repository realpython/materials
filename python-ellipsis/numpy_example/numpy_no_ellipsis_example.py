import numpy as np

# Three-dimensional array

dimensions = 3
items_per_dimension = 2
max_items = items_per_dimension**dimensions
axes = np.repeat(items_per_dimension, dimensions)

arr = np.arange(max_items).reshape(axes)

print(arr[:, :, 0])

# Multidimensional array

dimensions = 5  # np.random.randint(1,10)
items_per_dimension = 2
max_items = items_per_dimension**dimensions
axes = np.repeat(items_per_dimension, dimensions)

arr = np.arange(max_items).reshape(axes)

print(arr[..., 0])
