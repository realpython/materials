def format_name(first_name, last_name, /, title=None):
    full_name = f"{first_name} {last_name}"
    if title is not None:
        full_name = f"{title} {full_name}"
    return full_name


print(format_name("Jane", "Doe"))
print(format_name("John", "Doe", title="Dr."))
print(format_name("Linda", "Brown", "PhD."))
