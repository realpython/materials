import re

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

regex = re.compile(pattern)

text = """
    Please contact us at support@example.com
    or sales@example.com for further information.
"""

print(regex.findall(text))
