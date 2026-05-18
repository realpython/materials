# Avoid this:
# def read_first_line(file_path):
#     file = open(file_path, encoding="utf-8")
#     return file.readline().rstrip("\n")


# Favor this:
def read_first_line(path):
    with open(path, encoding="utf-8") as file:
        return file.readline().rstrip("\n")
