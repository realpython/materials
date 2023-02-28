import time
from itertools import cycle

for frame in cycle(r"-\|/-\|/"):
    print(frame, end="\b", flush=True)
    time.sleep(0.2)
