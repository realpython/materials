def read_temperature():
    return 25


if (temperature := read_temperature()) < 10:
    print("The weather is cold!")
elif 10 <= temperature <= 25:
    print("The weather is nice!")
else:
    print("The weather is hot!")
