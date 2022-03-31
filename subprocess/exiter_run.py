import subprocess

subprocess.run(["python", "exiter.py"], check=False)

try:
    subprocess.run(["python", "exiter.py"], check=True)
except subprocess.CalledProcessError as exc:
    print(exc)
