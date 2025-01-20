person = "Dr. Jane Doe, PhD Professor of Biology"

title, first_name, last_name, rest_info = person.split(maxsplit=3)

print(f"Title: {title}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Additional Info: {rest_info}")
