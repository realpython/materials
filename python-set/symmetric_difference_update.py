morning_attendees = {"Alice", "Charlie", "Linda", "John", "Jane"}
afternoon_attendees = {"Charlie", "Linda", "Bob", "Jane"}
whole_day_attendees = set()

whole_day_attendees ^= morning_attendees
print(whole_day_attendees)

whole_day_attendees.symmetric_difference_update(afternoon_attendees)
print(whole_day_attendees)
