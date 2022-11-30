"""
**Only works on Linux or macOS**

Demonstrates basic usage of `subprocess.run()`.
"""

import subprocess

subprocess.run(["sh", "-c", "ls"])

subprocess.run(["ls"], shell=True)
