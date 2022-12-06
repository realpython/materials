username = input("Username: ")
password = input("Password: ")

users = [("john", "secret"), ("jane", "secret"), ("linda", "secret")]

if (username, password) in users:
    print(f"Hi {username}, you're logged in!")
else:
    print("Wrong username or password")
