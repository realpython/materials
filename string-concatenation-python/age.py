def age_group(age):
    if age >= 0 and age <= 9:
        result = "a Child!"
    elif age > 9 and age <= 18:
        result = "an Adolescent!"
    elif age > 18 and age <= 65:
        result = "an Adult!"
    else:
        result = "a Golden ager!"
    print("You are " + result)
