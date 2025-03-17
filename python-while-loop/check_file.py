import time
from pathlib import Path

filename = Path("hello.txt")

print(f"Waiting for {filename.name} to be created...")

while not filename.exists():
    print("File not found. Retrying in 1 second...")
    time.sleep(1)

print(f"{filename} found! Proceeding with processing.")
with open(filename, mode="r") as file:
    print("File contents:")
    print(file.read())
