students = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
    "Fiona": 95.6,
    "George": 73.4,
    "Hannah": 81.2,
}
for student in students:
    print(student)

for student in students.keys():
    print(student)

for student in students:
    print(student, "->", students[student])

MLB_teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}
for team in MLB_teams.values():
    print(team)

for city, team in MLB_teams.items():
    print(city, "->", team)
