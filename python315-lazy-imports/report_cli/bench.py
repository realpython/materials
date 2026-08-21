"""Time how long a script takes to start, run, and exit.

Usage:

    python bench.py cli_eager.py --help

Runs the script ten times and reports the fastest run, which is the
measurement least polluted by whatever else the machine is doing.
"""

import subprocess
import sys
import time

RUNS = 10

def time_once(command):
    start = time.perf_counter()
    subprocess.run(command, capture_output=True, check=False)
    return time.perf_counter() - start

def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python bench.py <script.py> [args...]")

    script, *script_args = sys.argv[1:]
    command = [sys.executable, script, *script_args]

    best = min(time_once(command) for _ in range(RUNS))
    print(f"{script}: {best * 1000:.0f} ms (best of {RUNS})")

if __name__ == "__main__":
    main()
