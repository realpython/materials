import subprocess

# LINUX examples

subprocess.run(["sh", "ls"])

subprocess.run(["ls"], shell=True)
