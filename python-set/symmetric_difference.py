morning_attendees = {"Alice", "Charlie", "Linda", "John", "Jane"}
afternoon_attendees = {"Charlie", "Linda", "Bob", "Jane"}

print(morning_attendees ^ afternoon_attendees)
print(morning_attendees.symmetric_difference(afternoon_attendees))

a = {1, 2, 3, 4, 5}
b = {10, 2, 3, 4, 50}
c = {1, 50, 100}
print(a ^ b ^ c)
