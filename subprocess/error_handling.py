import subprocess

try:
    _ = subprocess.run(
        ["python", "custom_exit.py", "1"], check=True, capture_output=True
    )
except subprocess.CalledProcessError as exc:
    print(exc)


failed_process = subprocess.run(
    ["python", "custom_exit.py", "1"], capture_output=True
)

try:
    failed_process.check_returncode()
except subprocess.CalledProcessError as exc:
    print(exc)


try:
    _ = subprocess.run(
        ["python", "timer.py", "5"], capture_output=True, timeout=1
    )
except subprocess.TimeoutExpired as exc:
    print(exc)


try:
    _ = subprocess.run(["non_existent_program"])
except FileNotFoundError as exc:  # Subclass of OSError
    print(exc)


try:
    _ = subprocess.run(
        ["python", "non_existent_file"], check=True, capture_output=True
    )
except subprocess.CalledProcessError as exc:
    if exc.returncode == 2:
        print("Python couldn't find the file")
