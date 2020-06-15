# yang.py

print(f"Hello from yang")
import yin  # noqa

number = 24


def combine():
    return number + yin.number


print(f"yin and yang combined is {combine()}")
print(f"Goodbye from yang")
