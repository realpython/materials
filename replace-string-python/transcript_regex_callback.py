import re

ENTRY_PATTERN = (
    r"\[(.+)\] "  # User string, discarding square brackets
    r"[-T:+\d]{25} "  # Time stamp
    r": "  # Separator
    r"(.+)"  # Message
)
BAD_WORDS = ["blast", "dash", "beezlebub"]
CLIENTS = ["johndoe", "janedoe"]


def censor_bad_words(message):
    for word in BAD_WORDS:
        message = re.sub(rf"{word}\w*", "😤", message, flags=re.IGNORECASE)
    return message


def censor_users(user):
    if user.startswith("support"):
        return "Agent"
    elif user in CLIENTS:
        return "Client"
    else:
        raise ValueError(f"unknown client: '{user}'")


def sanitize_message(match):
    user, message = match.groups()
    return f"{censor_users(user):<6} : {censor_bad_words(message)}"


transcript = """
[support_tom] 2025-01-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2025-01-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2025-01-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2025-01-24T10:04:03+00:00 : Blast! You're right!
"""

print(re.sub(ENTRY_PATTERN, sanitize_message, transcript))
