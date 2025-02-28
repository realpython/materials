MAX_ATTEMPTS = 3

correct_password = "secret123"
attempts = 0


while True:
    password = input("Password: ").strip()
    attempts += 1

    if password == correct_password:
        print("Login successful! Welcome!")
        break

    if attempts >= MAX_ATTEMPTS:
        print("Too many failed attempts.")
        break
    else:
        print(f"Incorrect password. {MAX_ATTEMPTS - attempts} attempts left.")
