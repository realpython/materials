usernames = ["Alice", " bob", "ALICE  ", "Bob", "charlie", "Charlie", "JOHN"]
print({name.lower().strip() for name in usernames})
