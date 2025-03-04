user_input = "Amount to withdraw? "
amount = int(input(user_input))
available_balance = 1000
print(f"Here are your {amount:.2f}USD")
print(f"Your available balance is {available_balance - amount:.2f}USD")
