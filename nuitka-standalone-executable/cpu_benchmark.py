import math
import time

start = time.perf_counter()
total = 0.0
for i in range(20_000_000):
    total += math.sqrt(i)
elapsed = time.perf_counter() - start

print(f"Result: {total}")
print(f"Time: {elapsed:.3f}s")
