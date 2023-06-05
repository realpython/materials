import math

lam = 4
cars_per_minute = [0, 4, 8]

for cars in cars_per_minute:
    probability = lam**cars * math.exp(-lam) / math.factorial(cars)
    print(f"P({cars}) = {probability:.1%}")
