data = ["  Alice ", " Bob  ", " Charlie\n", "\tDora"]
cleaned_data = [name.strip() for name in data]
print(cleaned_data)
