class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = permissions


admin = User("admin", "wrx")
john = User("john", "rx")


def has_permission(user, permission):
    return permission in user.permissions


has_permission(admin, "w")
has_permission(john, "w")
