secret_message = "3LAigf7eq 5fhiOnpdDs2 Ra6 nwUalyo.9"
message = ""

for index, char in enumerate(secret_message):
    if index % 2:
        message += char

print(message)
