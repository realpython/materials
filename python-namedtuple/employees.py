import csv
from collections import namedtuple

with open("employees.csv", mode="r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    Employee = namedtuple("Employee", next(reader), rename=True)
    for row in reader:
        employee = Employee(*row)
        print(employee)
