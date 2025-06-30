lines = [
    "This is a\tline",
    "This line is fine",
    "Another line with whitespace ",
]

for lineno, line in enumerate(lines, start=1):
    if "\t" in line:
        print(f"Line {lineno}: Contains a tab character.")
    if line.rstrip() != line:
        print(f"Line {lineno}: Contains trailing whitespace.")
