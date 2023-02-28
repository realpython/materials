import sys
import time

# Experiment with changing this number to hone in on the buffer size
# on your operating system
SLIGHTLY_TOO_LARGE_FOR_BUFFER = 10_000

for x in range(SLIGHTLY_TOO_LARGE_FOR_BUFFER // 6):
    sys.stdout.write(f"{x:6}")

time.sleep(2)
