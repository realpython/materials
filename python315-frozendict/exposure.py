from decimal import Decimal


class BankAccount:
    def __init__(self):
        self._balances = {"USD": Decimal("0"), "EUR": Decimal("0")}

    @property
    def balances(self):
        return frozendict(self._balances)


account = BankAccount()
account.balances["USD"] = Decimal("1_000_000")
