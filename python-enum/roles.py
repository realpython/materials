from enum import Flag, IntFlag

# class Role(IntFlag):
#     OWNER = 8
#     POWER_USER = 4
#     USER = 2
#     SUPERVISOR = 1
#     ADMIN = OWNER | POWER_USER | USER | SUPERVISOR


class Role(Flag):
    OWNER = 8
    POWER_USER = 4
    USER = 2
    SUPERVISOR = 1
    ADMIN = OWNER | POWER_USER | USER | SUPERVISOR


john = Role.USER | Role.SUPERVISOR

if Role.USER in john:
    print("John, you're a user")

if Role.SUPERVISOR in john:
    print("John, you're a supervisor")
