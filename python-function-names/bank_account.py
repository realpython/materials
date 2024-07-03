class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __repr__(self):
        return f"{type(self).__name__}({self.account_number}, {self.balance})"

    def _verify_funds(self, amount):
        return self.balance >= amount

    def _deduct_funds(self, amount):
        self.balance -= amount

    def _add_funds(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self._verify_funds(amount):
            self._deduct_funds(amount)
            return True
        return False

    def deposit(self, amount):
        self._add_funds(amount)
        return True
