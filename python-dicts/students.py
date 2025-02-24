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
print(dict(sorted(students.items(), key=lambda item: item[1])))
print(dict(sorted(students.items(), key=lambda item: item[1], reverse=True)))
