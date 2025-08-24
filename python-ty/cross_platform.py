from sys import platform
from typing import reveal_type

if platform == "win32":
    x = "Windows"
else:
    x = "macOS or Linux"

reveal_type(x)
