import subprocess

subprocess.run(["python", "custom_exit.py", "5"], check=False)

try:
    subprocess.run(["python", "custom_exit.py", "5"], check=True)
except subprocess.CalledProcessError as exc:
    print(exc)
