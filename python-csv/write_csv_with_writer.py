import csv

with open("employee_file.csv", mode="w", newline="") as employee_file:
    employee_writer = csv.writer(
        employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )

    employee_writer.writerow(["John Smith", "Accounting", "November"])
    employee_writer.writerow(["Erica Meyers", "IT", "March"])
