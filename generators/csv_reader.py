def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row


csv_gen = csv_reader("techcrunch.csv")
row_count = 0
for row in csv_gen:
    row_count += 1
print(f"Row count is {row_count}")
