"""
Eager and lazy options for reading a CSV file
"""

import csv
import pprint

print("Eager evaluation using 'open()'")
with open("superhero_pets.csv", encoding="utf-8") as file:
    data = file.readlines()

pprint.pprint(data)

print("\nLazy evaluation using 'csv.reader()'")
with open("superhero_pets.csv", encoding="utf-8", newline="") as file:
    data = csv.reader(file)
    print(data)

    print(next(data))
    print(next(data))
    print(next(data))

    for row in data:
        print(row)
