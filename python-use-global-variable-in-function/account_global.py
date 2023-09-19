balance = 0


def deposit(amount):
    global balance
    balance += amount
    print(f"Successful deposit: +${amount:,.2f}")


def withdraw(amount):
    global balance
    if balance - amount > 0:
        balance -= amount
        print(f"Successful withdrawal: -${amount:,.2f}")
    else:
        print("Not enough funds for this transaction")


def get_balance():
    return balance


def main():
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
            deposit(amount)
        elif operation in "wW":
            amount = float(input("Enter the withdrawal amount: "))
            withdraw(amount)
        elif operation in "bB":
            print(f"Current balance: ${get_balance():,.2f}")
        elif operation in "qQ":
            print("Goodbye!")
            break
        else:
            print("Invalid operation. Please try again.")


main()
