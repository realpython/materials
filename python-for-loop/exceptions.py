files = ["file1.txt", "file2.txt", "file3.txt"]

for file in files:
    with open(file, "r") as f:
        print(f"Contents of {file}:")
        print(f.read())

for file in files:
    try:
        with open(file, "r") as f:
            print(f"Contents of {file}:")
            print(f.read())
    except FileNotFoundError:
        print(f"Error: {file} not found. Skipping.")
