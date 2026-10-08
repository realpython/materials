import csv

with open("employee_file2.csv", mode="w", newline="") as csv_file:
    fieldnames = ["emp_name", "dept", "birth_month"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(
        {
            "emp_name": "John Smith",
            "dept": "Accounting",
            "birth_month": "November",
        }
    )
    writer.writerow(
        {"emp_name": "Erica Meyers", "dept": "IT", "birth_month": "March"}
    )
