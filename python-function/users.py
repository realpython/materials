def find_user(username, user_list):
    for user in user_list:
        if user["username"] == username:
            return user
    return None


users = [
    {"username": "alice", "email": "alice@example.com"},
    {"username": "bob", "email": "bob@example.com"},
]

find_user("alice", users)

print(find_user("linda", users))
