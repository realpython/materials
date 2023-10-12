from datetime import datetime

balance = 5425.9292
print(f"Balance: ${balance:.2f}")

heading = "Centered string"
print(f"{heading:=^30}")

integer = -1234567
print(f"Comma as thousand separators: {integer:,}")
sep = "_"
print(f"User's thousand separators: {integer:{sep}}")

floating_point = 1234567.9876
print(f"Comma as thousand separators and two decimals: {floating_point:,.2f}")

date = (9, 6, 2023)
print(f"Date: {date[0]:02}-{date[1]:02}-{date[2]}")

date = datetime(2023, 9, 26)
print(f"Date: {date:%m/%d/%Y}")
