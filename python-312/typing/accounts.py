import random
from dataclasses import dataclass
from typing import Self, override


def generate_account_number() -> str:
    """Generate a random eleven-digit account number"""
    accno = str(random.randrange(10_000_000_000, 100_000_000_000))
    return f"{accno[:4]}.{accno[4:6]}.{accno[6:]}"


@dataclass
class BankAccount:
    account_number: str
    balance: float

    @classmethod
    def from_balance(cls, balance: float) -> Self:
        return cls(generate_account_number(), balance)

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        self.balance -= amount


@dataclass
class SavingsAccount(BankAccount):
    interest: float

    def add_interest(self) -> None:
        self.balance *= 1 + self.interest / 100

    @classmethod
    @override
    def from_balance(cls, balance: float, interest: float = 1.0) -> Self:
        return cls(generate_account_number(), balance, interest)

    @override
    def withdraw(self, amount: float) -> None:
        self.balance -= int(amount) if amount > 100 else amount
