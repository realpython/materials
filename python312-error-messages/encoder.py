from this import d

message = "Thanks for all the added clarity in error messages, Pablo!"

reverse_cypher_dict = {value: key for key, value in d.items()}

encoded_message = ""
for character in message:
    if character.isalpha():
        encoded_message += reverse_cypher_dict.get(character, "")
    else:
        encoded_message += character

print(encoded_message)
