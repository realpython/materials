import pyinputplus as pyip

age = pyip.inputInt(prompt="Enter your age: ", min=0, max=120)
print(f"Your age is: {age}")
