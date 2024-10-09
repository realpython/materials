import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

customer_available_condition = threading.Condition()

# Customers waiting to be served by the Teller
customer_queue = []


def serve_customers():
    while True:
        with customer_available_condition:
            # Wait for a customer to arrive
            while not customer_queue:
                print(f"{int(time.time())}: Teller is waiting for a customer.")
                customer_available_condition.wait()

            # Serve the customer
            customer = customer_queue.pop(0)
            print(f"{int(time.time())}: Teller is serving {customer}.")

        # Simulate the time taken to serve the customer
        time.sleep(random.randint(1, 3))
        print(f"{int(time.time())}: Teller has finished serving {customer}.")


def add_customer_to_queue(name):
    with customer_available_condition:
        print(f"{int(time.time())}: {name} has arrived at the bank.")
        customer_queue.append(name)

        customer_available_condition.notify()


customer_names = [
    "Customer 1",
    "Customer 2",
    "Customer 3",
    "Customer 4",
    "Customer 5",
]

with ThreadPoolExecutor(max_workers=6) as executor:

    teller_thread = executor.submit(serve_customers)

    for name in customer_names:
        # Simulate customers arriving at random intervals
        time.sleep(random.randint(2, 5))

        executor.submit(add_customer_to_queue, name)
