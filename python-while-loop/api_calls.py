import random
import time


def is_api_available():
    """Simulate API availability."""
    return random.choice([True, False, False, False])


def make_api_call(request):
    print(f"Making API call: {request}")
    time.sleep(0.5)


requests = iter(["Request 1", "Request 2", "Request 3"])
request = next(requests)

while True:
    if not is_api_available():
        print("API not available. Retrying in 1 sec...")
        time.sleep(1)
        continue
    make_api_call(request)
    try:
        request = next(requests)
    except StopIteration:
        break

print("All requests processed.")
