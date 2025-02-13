import random
import time

MAX_RETRIES = 5
attempts = 0

while attempts < MAX_RETRIES:
    attempts += 1
    print(f"Attempt {attempts}: Connecting to the server...")
    # Simulating a connection scenario
    time.sleep(0.5)
    if random.choice([False, False, False, True]):
        print("Connection successful!")
        break

    print("Connection failed. Retrying...")
else:
    print("All attempts failed. Unable to connect.")
