employees = [
    ("John", 30, "Designer", 75000),
    ("Jane", 28, "Engineer", 60000),
    ("Bob", 35, "Analyst", 50000),
    ("Mary", 25, "Service", 40000),
    ("Tom", 40, "Director", 90000),
]


sorted_employees = sorted(employees, key=lambda e: e[1])
