import time
from concurrent.futures import ThreadPoolExecutor


class BankAccount:
    def __init__(self):
        self.balance = 1000

    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            time.sleep(0.1)  # Simulate a delay
            self.balance = new_balance
        else:
            raise Exception("Insufficient balance")


account = BankAccount()

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(account.withdraw, 500)
    executor.submit(account.withdraw, 700)

print(f"Final account balance: {account.balance}")
