# Poorly-named function, parameter, and variable
def init(n):
    return " ".join(f"{i[0]}." for i in n.split())


# Descriptive names improve readability
def get_initials(full_name):
    return " ".join(f"{name[0]}." for name in full_name.split())


print(get_initials("James Clerk Maxwell"))
# OUTPUT: J. C. M.
print(get_initials("Richard Feynman"))
# OUTPUT: R. F.
