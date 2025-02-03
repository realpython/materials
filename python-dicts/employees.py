from collections import defaultdict

employees = [
    ("Sales", "John"),
    ("Sales", "Martin"),
    ("Accounting", "Kate"),
    ("Marketing", "Elizabeth"),
    ("Marketing", "Linda"),
]

departments = defaultdict(list)
for department, employee in employees:
    departments[department].append(employee)

print(departments)
