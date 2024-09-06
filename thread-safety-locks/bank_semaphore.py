import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Semaphore with a maximum of 2 resources (tellers)
teller_semaphore = threading.Semaphore(2)


def serve_customer(name):
    print(f"{int(time.time())}: {name} is waiting for a teller.")
    with teller_semaphore:
        print(f"{int(time.time())}: {name} is being served by a teller.")
        # Simulate the time taken for the teller to serve the customer
        time.sleep(random.randint(1, 3))
        print(f"{int(time.time())}: {name} is done being served.")


customers = [
    "Customer 1",
    "Customer 2",
    "Customer 3",
    "Customer 4",
    "Customer 5",
]

with ThreadPoolExecutor(max_workers=5) as executor:
    for customer_name in customers:
        thread = executor.submit(serve_customer, customer_name)


print("All customers have been served.")
