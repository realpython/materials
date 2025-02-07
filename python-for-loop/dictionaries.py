students = {
    "Alice": 89.5,
    "Bob": 76.0,
    "Charlie": 92.3,
    "Diana": 84.7,
    "Ethan": 88.9,
}
for student in students:
    print(student)

for student in students:
    print(student, "->", students[student])

for student in students.keys():
    print(student)

teams = {
    "Colorado": "Rockies",
    "Chicago": "White Sox",
    "Boston": "Red Sox",
    "Minnesota": "Twins",
    "Milwaukee": "Brewers",
    "Seattle": "Mariners",
}
for team in teams.values():
    print(team)

for place, team in teams.items():
    print(place, "->", team)
