"""
Accepts an integer argument and will sleep for the given time. For example:

```
$ python timer.py 5
Starting timer of 5 seconds
.....Done!
```
"""

from argparse import ArgumentParser
from time import sleep

parser = ArgumentParser()
parser.add_argument("time", type=int)
args = parser.parse_args()
print(f"Starting timer of {args.time} seconds")
for _ in range(args.time):
    print(".", end="", flush=True)
    sleep(1)
print("Done!")
