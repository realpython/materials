import subprocess

# LINUX examples

subprocess.run(["sh", "-c", "ls"])

subprocess.run(["ls"], shell=True)
