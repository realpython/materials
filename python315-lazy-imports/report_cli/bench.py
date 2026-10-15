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

if sys.version_info < (3, 15):
    sys.exit(
        "The report CLI needs Python 3.15 or later for the lazy "
        f"keyword, but this is {sys.version.split()[0]}."
    )

def time_once(command):
    start = time.perf_counter()
    process = subprocess.run(command, capture_output=True, text=True)
    elapsed = time.perf_counter() - start
    if process.returncode != 0:
        sys.exit(
            f"{command[1]} exited with code {process.returncode}, so "
            f"there's nothing meaningful to time:\n{process.stderr}"
        )
    return elapsed

def main():
    if len(sys.argv) < 2:
        sys.exit("usage: python bench.py <script.py> [args...]")

    script, *script_args = sys.argv[1:]
    command = [sys.executable, script, *script_args]

    best = min(time_once(command) for _ in range(RUNS))
    print(f"{script}: {best * 1000:.0f} ms (best of {RUNS})")

if __name__ == "__main__":
    main()
