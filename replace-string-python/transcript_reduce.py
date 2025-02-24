from functools import reduce

REPLACEMENTS = [
    ("BLASTED", "😤"),
    ("Blast", "😤"),
    ("2025-01-24T", ""),
    ("+00:00", ""),
    ("[support_tom]", "Agent "),
    ("[johndoe]", "Client"),
]

transcript = """
[support_tom] 2025-01-24T10:02:23+00:00 : What can I help you with?
[johndoe] 2025-01-24T10:03:15+00:00 : I CAN'T CONNECT TO MY BLASTED ACCOUNT
[support_tom] 2025-01-24T10:03:30+00:00 : Are you sure it's not your caps lock?
[johndoe] 2025-01-24T10:04:03+00:00 : Blast! You're right!
"""

print(reduce(lambda acc, item: acc.replace(*item), REPLACEMENTS, transcript))
