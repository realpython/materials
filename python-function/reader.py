from pathlib import Path


def read_file_contents(file_path):
    path = Path(file_path)

    if not path.exists():
        print(f"Error: The file '{file_path}' does not exist.")
        return

    if not path.is_file():
        print(f"Error: '{file_path}' is not a file.")
        return

    return path.read_text(encoding="utf-8")
