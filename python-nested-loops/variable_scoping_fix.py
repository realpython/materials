employees = [("Dorothy", "DevOps"), ("Abdel", "HR"), ("Nataliya", "DevOps")]
departments = [
    {"name": "DevOps", "city": "Berlin"},
    {"name": "HR", "city": "Abuja"},
]

for name, department in employees:
    for dept in departments:
        if dept["name"] == department:
            print(f"{name} works in {dept['city']}")
