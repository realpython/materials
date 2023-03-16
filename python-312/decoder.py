from this import d

message = "Gunaxf sbe nyy gur nqqrq pynevgl va reebe zrffntrf, Cnoyb!"

decoded_characters = []
for character in message:
    if character.isalpha():
        decoded_characters.append(d.get(character, ""))
    else:
        decoded_characters.append(character)
decoded_message = "".join(decoded_characters)

print(decoded_message)
