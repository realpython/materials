"""
Demonstrates error handling with `subprocess.run()`, catching common errors
that `subprocess.run()` can encounter. Try changing the commands in
`subprocess.run()` to raise different errors.
"""

import subprocess

try:
    subprocess.run(["python", "timer.py", "10"], timeout=5, check=True)
except FileNotFoundError as exc:
    print(f"Process failed because the executable could not be found.\n{exc}")
except subprocess.CalledProcessError as exc:
    print(
        f"Process failed because did not return a successful return code. "
        f"Returned {exc.returncode}\n{exc}"
    )
except subprocess.TimeoutExpired as exc:
    print(f"Process timed out.\n{exc}")
