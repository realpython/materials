submitted_username = "_!__YoJohnDoe!__!!"
cleaned_username = submitted_username.strip("!_")
print(cleaned_username)

# Order of characters doesn't matter
print(submitted_username.strip("_!"))
