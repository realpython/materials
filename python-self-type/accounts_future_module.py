from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass
class BankAccount:
    account_number: int
    balance: float

    def display_balance(self) -> BankAccount:
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:,.2f}\n")
        return self

    def deposit(self, amount: float) -> BankAccount:
        self.balance += amount
        return self

    def withdraw(self, amount: float) -> BankAccount:
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")
        return self


@dataclass
class SavingsAccount(BankAccount):
    interest_rate: float

    @classmethod
    def from_application(
        cls, deposit: float = 0, interest_rate: float = 1
    ) -> SavingsAccount:
        # Generate a random seven-digit bank account number
        account_number = random.randint(1000000, 9999999)
        return cls(account_number, deposit, interest_rate)

    def calculate_interest(self) -> float:
        return self.balance * self.interest_rate / 100

    def add_interest(self) -> SavingsAccount:
        self.deposit(self.calculate_interest())
        return self


account = BankAccount(account_number=1534899324, balance=50)
(
    account.display_balance()
    .deposit(50)
    .display_balance()
    .withdraw(30)
    .display_balance()
)

savings = SavingsAccount.from_application(deposit=100, interest_rate=5)
(
    savings.display_balance()
    .add_interest()
    .display_balance()
    .deposit(50)
    .display_balance()
    .withdraw(30)
    .add_interest()
    .display_balance()
)
