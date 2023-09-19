from this import d

message = "Thanks for all the added clarity in error messages, Pablo!"

reverse_cypher_dict = {value: key for key, value in d.items()}

encoded_characters = []
for character in message:
    if character.isalpha():
        encoded_characters.append(reverse_cypher_dict.get(character, ""))
    else:
        encoded_characters.append(character)

encoded_message = "".join(encoded_characters)

print(encoded_message)
