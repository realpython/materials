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


def make_recursive_nested_dir(
    dir_name, levels, number_of_folders_per_level, number_of_files_per_folder
):
    nested_dir = pathlib.Path(dir_name)
    nested_dir.mkdir()

    def helper(dir, levels, number_of_folders, number_of_files):
        for file_number in range(number_of_files):
            pathlib.Path(dir / pathlib.Path(f"{file_number}.txt")).touch()

        if levels < 1:
            return

        for folder_number in range(number_of_folders):
            folder = pathlib.Path(
                dir / pathlib.Path(f"folder_{folder_number}")
            )
            folder.mkdir()
            helper(folder, levels - 1, number_of_folders, number_of_files)

    helper(
        nested_dir,
        levels,
        number_of_folders_per_level,
        number_of_files_per_folder,
    )

    return nested_dir


def recursive_rmdir(directory):
    """Or just use shutil.rmtree()"""
    for item in directory.iterdir():
        if item.is_dir():
            recursive_rmdir(item)
        else:
            item.unlink()
    directory.rmdir()
