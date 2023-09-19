data = [
    ["Name", "Age", "Hometown"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "Los Angeles"],
    ["Charlie", "35", "Chicago"],
]


def display_table(data):
    max_len = max(len(header) for header in data[0])
    sep = "-" * max_len
    for row in data:
        print("|".join(header.ljust(max_len) for header in row))
        if row == data[0]:
            print("|".join(sep for _ in row))


display_table(data)
