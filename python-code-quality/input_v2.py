user_input = "Amount to withdraw? "
amount = int(input(user_input))
available_balance = 1000
if amount > available_balance:
    print("Insufficient funds")
    amount = 0
else:
    print(f"Here are your {amount:.2f}USD")

print(f"Your available balance is {available_balance - amount:.2f}USD")
