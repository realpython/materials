employees = [("Dorothy", "DevOps"), ("Abdel", "HR"), ("Nataliya", "DevOps")]
departments = [
    {"name": "DevOps", "city": "Berlin"},
    {"name": "HR", "city": "Abuja"},
]

for name, department in employees:
    for department in departments:
        if department["name"] == department:
            print(f"{name} works in {department['city']}")
