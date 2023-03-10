from this import d

message = "Gunaxf sbe nyy gur nqqrq pynevgl va reebe zrffntrf, Cnoyb!"

decoded_message = ""
for character in message:
    if character.isalpha():
        decoded_message += d.get(character, "")
    else:
        decoded_message += character

print(decoded_message)
