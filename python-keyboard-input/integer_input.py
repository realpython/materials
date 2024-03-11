while True:
    try:
        age = int(input("How old are you? "))
    except ValueError:
        print("Please enter a number for your age.")
    else:
        break
print(f"Next year, you'll be {age + 1} years old")
