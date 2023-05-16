import numpy as np

lam = 4
cars_per_minute = [0, 4, 8]

for cars in cars_per_minute:
    probabil = np.exp(-lam) * np.power(lam, cars) / np.math.factorial(cars)
    print(f"P({cars}) = {round(probabil * 100, 1)}%")
