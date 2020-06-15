# yang.py

print("Hello from yang")
import yin  # noqa

number = 24


def combine():
    return number + yin.number


print(f"yin and yang combined is {combine()}")
print("Goodbye from yang")
