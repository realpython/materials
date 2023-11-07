import numpy as np

# Create vectors with NumPy
vector1 = np.array([1, 0])
vector2 = np.array([0, 1])
print(vector1)
print(vector2)

v1 = np.array([1, 0])
v2 = np.array([0, 1])
v3 = np.array([np.sqrt(2), np.sqrt(2)])

# Dimension
print(v1.shape)

# Magnitude
print(np.sqrt(np.sum(v1**2)))
print(np.linalg.norm(v1))
print(np.linalg.norm(v3))

# Dot product
print(np.sum(v1 * v2))
print(v1 @ v3)
