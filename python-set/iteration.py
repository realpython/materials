employees = {"Alice", "Charlie", "John", "Laura"}
for employee in employees:
    print(f"Hello, {employee}!")

employees = {"Alice", "Charlie", "John", "Laura"}
uppercase = set()
for employee in employees:
    uppercase.add(employee.upper())

print(uppercase)

employees = {"Alice", "Charlie", "John", "Laura"}
employees = {employee.upper() for employee in employees}
print(employees)

available_seats = {"A1", "A2", "B1", "B2", "C1"}
while available_seats:
    assigned_seat = available_seats.pop()
    print(f"Seat {assigned_seat} was assigned")

print(available_seats)

cities = {"Vancouver", "Berlin", "London", "Warsaw", "Vienna"}
for city in sorted(cities):
    print(city)

cities = {
    ("Vancouver", 675000),
    ("Berlin", 3800000),
    ("London", 8980000),
    ("Warsaw", 1790000),
    ("Vienna", 1900000),
}
for city in sorted(cities, key=lambda city: city[1]):
    print(city)

for city in sorted(cities, key=lambda city: city[1], reverse=True):
    print(city)
