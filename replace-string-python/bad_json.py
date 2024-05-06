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


try_decode(data)


print(re.sub(pattern=r"(.+)(=)(.+)", repl=r'"\1":"\3"', string=data))
try_decode(data)


data = re.sub(pattern=r"\s+(.+)(\s+=\s+)(.+)", repl=r'"\1":"\3",', string=data)
print(data)
try_decode(data)


# Remove last comma
data = re.sub(pattern=r",$", repl="", string=data, flags=re.MULTILINE)
print(data)
data = try_decode(data)
