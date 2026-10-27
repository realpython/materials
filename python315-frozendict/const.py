ROLE_PERMISSIONS = frozendict(
    viewer=frozenset({"read"}),
    editor=frozenset({"read", "write"}),
    admin=frozenset({"read", "write", "delete", "manage_users"}),
)

print(ROLE_PERMISSIONS)
