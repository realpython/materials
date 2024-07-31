def display_table(data, headers):
    max_len = max(len(header) for header in headers)
    print(" | ".join(header.ljust(max_len) for header in headers))
    sep = "-" * max_len
    print("-|-".join(sep for _ in headers))
    for row in data:
        print(" | ".join(header.ljust(max_len) for header in row))


data = [
    ["Alice", "25", "Python Developer"],
    ["Bob", "30", "Web Designer"],
    ["Charlie", "35", "Team Lead"],
]

headers = ["Name", "Age", "Job Title"]

display_table(data, headers)
