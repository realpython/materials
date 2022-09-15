name_list = [False, None, 0, "Linda", "Tiffany", "Florina", "Jovann"]
empty_list = []
no_list = None
long_name_list = [
    "Ainslie",
    "Dieter",
    "Gabey",
    "Carena",
    "Allina",
    "Aila",
    "Quent",
    "Joanie",
    "Gypsy",
    "Stafford",
    "Harlan",
    "Addy",
    "Florina",
    "Mindy",
    "Tracy",
    "Mame",
    "Rustin",
]

name_lists = [name_list, empty_list, no_list, long_name_list]


def build_list(size, fill, value, at_position):
    return [fill if i != at_position else value for i in range(size)]
