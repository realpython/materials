import csv

with open("employee_birthday.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Column names are {', '.join(row)}")
            line_count += 1
        print(
            f"\t{row['name']} works in the {row['department']} "
            f"department, and was born in {row['birthday month']}."
        )
        line_count += 1
    print(f"Processed {line_count} lines.")
