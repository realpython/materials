import re

transcript = """
[support_tom] 2022-08-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2022-08-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2022-08-24T10:03:30+00:00 : Are you sure it's not your caps-lock?
[johndoe] 2022-08-24T10:04:03+00:00 : Blast! You're right!
"""

regex_replacements = [
    (r"blast\w*", "😤"),
    (r" [-T:\+\d]{25}", ""),
    (r"\[support\w*\]", "Agent"),
    (r"\[johndoe\]", "Client"),
]

for regex_find, regex_replace in regex_replacements:
    transcript = re.sub(
        regex_find, regex_replace, transcript, flags=re.IGNORECASE
    )

print(transcript)
