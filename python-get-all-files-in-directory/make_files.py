import pathlib


def make_dir_with_files(dir_name, number_of_files):
    flat_dir = pathlib.Path(dir_name)
    flat_dir.mkdir()

    for file_number in range(number_of_files):
        pathlib.Path(flat_dir / pathlib.Path(f"{file_number}.txt")).touch()
    return flat_dir


def make_nested_dir(
    dir_name, number_of_folders, number_of_files_in_subfolders
):
    nested_dir = pathlib.Path(dir_name)
    nested_dir.mkdir()

    for folder_number in range(number_of_folders):
        folder = pathlib.Path(nested_dir / pathlib.Path(f"{folder_number}"))
        folder.mkdir()
        for file_number in range(number_of_files_in_subfolders):
            pathlib.Path(folder / pathlib.Path(f"{file_number}.txt")).touch()

    return nested_dir
