import csv
from typing import NamedTuple


class Employee(NamedTuple):
    name: str
    age: int
    position: str = "Python Developer"


with open("employees.csv", mode="r") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip headers
    employees = []
    for name, age, position in reader:
        employees.append(Employee(name, int(age), position))
