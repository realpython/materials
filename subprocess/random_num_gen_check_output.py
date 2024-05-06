"""
Uses `subprocess.run()` to call [random_num_gen.py](random_num_gen.py) to
generate a random number, read the output, and then print it.
"""

import subprocess

process = subprocess.run(
    ["python", "random_num_gen.py"], capture_output=True, text=True
)

print(int(process.stdout))
