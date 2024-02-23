import pyinputplus as pyip

account_balance = 1000

print("Welcome to REALBank.")
while True:
    print(f"\nYour account balance: ${account_balance}")
    transaction_type = pyip.inputChoice(["Deposit", "Withdraw", "Exit"])

    if transaction_type == "Exit":
        break
    elif transaction_type == "Deposit":
        deposit_amount = pyip.inputInt(
            prompt="Enter amount (max $10,000): $", min=0, max=10000
        )
        account_balance += deposit_amount
        print(f"Deposited ${deposit_amount}.")
    elif transaction_type == "Withdraw":
        withdrawal_amount = pyip.inputInt(
            prompt="Enter amount: $", min=0, max=account_balance
        )
        account_balance -= withdrawal_amount
        print(f"Withdrew ${withdrawal_amount}.")

print("\nThank you for choosing REALBank. We hope to see you again soon!")
