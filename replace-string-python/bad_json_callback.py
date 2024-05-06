import json
import re

data = """{
    birthday = 1991
    name = Python
    creator = Guido van Rossum
}"""


def try_decode(data):
    print("Trying to decode...")
    try:
        output = json.loads(data)
        print("success")
        return output
    except json.decoder.JSONDecodeError as e:
        print("FAIL")
        print(e)


def cleaner(match):
    return f'"{match.group(1).strip()}":"{match.group(3).strip()}",'


data = re.sub(pattern=r"(.+)(=)(.+)", repl=cleaner, string=data)
print(data)

# Remove last comma
data = re.sub(pattern=r",(\s)+}", repl="}", string=data, flags=re.MULTILINE)
print(data)

try_decode(data)
