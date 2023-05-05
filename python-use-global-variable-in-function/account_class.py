class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Successful deposit: +${amount:,.2f}")

    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
            print(f"Successful withdrawal: -${amount:,.2f}")
        else:
            print("Not enough funds for this transaction")


def main():
    account = Account()
    while True:
        operation = input(
            "What would you like to do?\n"
            " d) deposit  "
            " w) withdraw  "
            " b) balance  "
            " q) quit\n"
            "> "
        )
        if operation in "dD":
            amount = float(input("Enter the deposit amount: "))
            account.deposit(amount)
        elif operation in "wW":
            amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
        elif operation in "bB":
            print(f"Current balance: ${account.balance:,.2f}")
        elif operation in "qQ":
            print("Goodbye!")
            break
        else:
            print("Invalid operation. Please try again.")


main()
