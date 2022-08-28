import numpy as np

# Three dimensional array

dimensions = 3
items_per_array = 2
max_items = items_per_array**dimensions
axes = np.repeat(items_per_array, dimensions)

arr = np.arange(max_items).reshape(axes)

print(arr[:, :, 0])

# Multi dimensional array

dimensions = 5  # np.random.randint(1,10)
items_per_array = 2
max_items = items_per_array**dimensions
axes = np.repeat(items_per_array, dimensions)

arr = np.arange(max_items).reshape(axes)

print(arr[..., 0])
