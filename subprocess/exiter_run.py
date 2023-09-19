"""
Calls [custom_exit.py](custom_exit.py) with `subprocess.run()`,
demonstrating the `check` argument to `.run()`.
"""

import subprocess

subprocess.run(["python", "custom_exit.py", "5"], check=False)

try:
    subprocess.run(["python", "custom_exit.py", "5"], check=True)
except subprocess.CalledProcessError as exc:
    print(exc)
