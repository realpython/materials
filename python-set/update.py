checked_in_attendees = set()
print(id(checked_in_attendees))

checked_in_attendees |= {"Alice", "Charlie"}
print(checked_in_attendees)
print(id(checked_in_attendees))

checked_in_attendees.update({"Linda", "Bob"})
print(checked_in_attendees)
print(id(checked_in_attendees))
