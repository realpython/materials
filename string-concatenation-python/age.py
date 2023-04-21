def age_group(age):
    if 0 <= age <= 9:
        result = "a Child!"
    elif 9 < age <= 18:
        result = "an Adolescent!"
    elif 19 < age <= 65:
        result = "an Adult!"
    else:
        result = "in your Golden Years!"
    print("You are " + result)
