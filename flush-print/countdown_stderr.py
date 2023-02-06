import sys
from time import sleep

for i in range(3, 0, -1):
    print(i, end=" ", flush=True)
    print(f"[State: '{i}']", file=sys.stderr, end=" ")
    sleep(1)
print("Go!")
