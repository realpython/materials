import threading
import time
from concurrent.futures import ThreadPoolExecutor

bank_open = threading.Event()
transactions_open = threading.Event()


def serve_customer(customer_data):
    print(f"{customer_data['name']} is waiting for the bank to open.")

    bank_open.wait()
    print(f"{customer_data['name']} entered the bank")
    if customer_data["type"] == "WITHDRAW_MONEY":
        print(f"{customer_data['name']} is waiting for transactions to open.")
        transactions_open.wait()
        print(f"{customer_data['name']} is starting their transaction.")

        # Simulate the time taken for performing the transaction
        time.sleep(2)

        print(f"{customer_data['name']} completed transaction and exited bank")
    else:
        # Simulate the time taken for banking
        time.sleep(2)
        print(f"{customer_data['name']} has exited bank")


customers = [
    {"name": "Customer 1", "type": "WITHDRAW_MONEY"},
    {"name": "Customer 2", "type": "CHECK_BALANCE"},
    {"name": "Customer 3", "type": "WITHDRAW_MONEY"},
    {"name": "Customer 4", "type": "WITHDRAW_MONEY"},
]

with ThreadPoolExecutor(max_workers=4) as executor:
    for customer_data in customers:
        executor.submit(serve_customer, customer_data)

    print("Bank manager is preparing to open the bank.")
    time.sleep(2)
    print("Bank is now open!")
    bank_open.set()  # Signal that the bank is open

    time.sleep(3)
    print("Transactions are now open!")
    transactions_open.set()


print("All customers have completed their transactions.")
