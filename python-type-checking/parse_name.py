# parse_name.py

import parse


def parse_name(text: str) -> str:
    patterns = (
        "my name is {name}",
        "i'm {name}",
        "i am {name}",
        "call me {name}",
        "{name}",
    )
    for pattern in patterns:
        result = parse.parse(pattern, text)
        if result:
            return result["name"]
    return ""


answer = input("What is your name? ")
name = parse_name(answer)
print(f"Hi {name}, nice to meet you!")
