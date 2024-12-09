phone_numbers = [
    "54123",
    "54123",
    "54123",
    "54456",
    "54789",
    "54789",
]
for phone_number in phone_numbers[:]:
    if phone_numbers.count(phone_number) > 1:
        phone_numbers.remove(phone_number)
print(phone_numbers)


phone_numbers = [
    "54123",
    "54123",
    "54123",
    "54456",
    "54789",
    "54789",
]
phone_numbers = list(dict.fromkeys(phone_numbers))
print(phone_numbers)

phone_numbers = [
    "54123",
    "54123",
    "54123",
    "54456",
    "54789",
    "54789",
]
set(phone_numbers)
print(phone_numbers)
