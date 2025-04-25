registered_users = {"Alice", "Bob", "Charlie", "Diana", "Linda"}
checked_in_users = {"Alice", "Charlie", "Linda"}
print(registered_users - checked_in_users)
print(registered_users.difference(checked_in_users))

a = {1, 2, 3, 30, 300}
b = {10, 20, 30, 40}
c = {100, 200, 300, 400}
print(a - b - c)
print(a.difference(b, c))
