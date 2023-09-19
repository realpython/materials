import functools
from time import sleep

unbuffered_print = functools.partial(print, flush=True)

for second in range(3, 0, -1):
    unbuffered_print(second)
    sleep(1)
print("Go!")
