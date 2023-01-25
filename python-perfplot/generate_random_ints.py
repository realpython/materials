import random
import json

random_ints = [random.randint(0, 10_000) for _ in range(2**25)]

with open("random_ints.txt", mode="w", encoding="utf-8") as file:
    file.write(json.dumps(random_ints))

reverse_sorted = list(range(2**25, -1, -1))

with open("reverse_sorted.txt", mode="w", encoding="utf-8") as file:
    file.write(json.dumps(random_ints))
