import re

transcript = """
[support_tom] 2022-08-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2022-08-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2022-08-24T10:03:30+00:00 : Are you sure it's not your caps-lock?
[johndoe] 2022-08-24T10:04:03+00:00 : Blast! You're right!
"""

new_transcript = re.sub(r" blast\w*", "😤", transcript, flags=re.IGNORECASE)
new_transcript = re.sub(r" [-T:\+\d]{25}", "", new_transcript)
new_transcript = re.sub(r"\[support\w*\]", "Agent", new_transcript)
new_transcript = re.sub(r"\[johndoe\]", "Client", new_transcript)

print(new_transcript)
