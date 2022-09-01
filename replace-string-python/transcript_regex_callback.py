import re

transcript = """
[support_tom] 2022-08-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2022-08-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2022-08-24T10:03:30+00:00 : Are you sure it's not your caps-lock?
[johndoe] 2022-08-24T10:04:03+00:00 : Blast! You're right!
"""

message_pattern = r"(\[.+\]) ([-T:\+\d]{25}) : (.+)"

BAD_WORDS = ["blast", "dash", "beezlebub"]
CLIENTS = ["johndoe", "janedoe"]


def censor_bad_words(message):
    for word in BAD_WORDS:
        message = re.sub(rf"{word}\w*", "😤", message, flags=re.IGNORECASE)
    return message


def censor_clients(user):
    for client in CLIENTS:
        user = re.sub(rf"{client}", "Client", user)
    return user


def sanitize_message(match):
    user, _, message = match.groups()
    user = re.sub(r"\[.*support.*\]", "Agent", user)
    return f"{censor_clients(user)} : {censor_bad_words(message)}"


print(re.sub(message_pattern, sanitize_message, transcript))
