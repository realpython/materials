import pathlib
from pprint import pp

# Create a Path object
desktop = pathlib.Path("Desktop")

# Basic listing using .iterdir()
pp(list(desktop.iterdir()))

# Iteration to filter or process
for item in desktop.iterdir():
    print(f"{item} - {'dir' if item.is_dir() else 'file'}")

# Usage in a comprehension
pp([item for item in desktop.iterdir() if item.is_dir()])

# Basic listing using glob patterns
pp(list(desktop.glob("*")))
pp(list(desktop.glob("real*")))
pp(list(desktop.glob("*.txt")))

# Recursive listing
pp(list(desktop.rglob("*.py")))
pp(list(desktop.glob("**/*")))
pp(list(desktop.glob("**/*.py")))

# Recursive listing with more advanced checking
pp([list(filter(lambda item: item.is_file(), desktop.rglob("*")))])
pp([file for file in desktop.rglob("*") if file.suffix in [".py", ".md"]])
pp([file for file in desktop.rglob("*") if file.is_dir()])


# Recursive .iterdir() function to return items if they are files
def get_all_files(root: pathlib.Path):
    for item in root.iterdir():
        if item.is_file():
            yield item
        else:
            yield from get_all_files(item)


pp(list(get_all_files(desktop)))


# Recursive .iterdir() function to rename txt files to md files
def rename_txt_to_md(root: pathlib.Path):
    for item in root.iterdir():
        if item.is_file() and item.suffix == ".txt":
            item.rename(f"{item.parent}/{item.stem}.md")
        elif item.is_dir():
            rename_txt_to_md(item)


# rename_txt_to_md(desktop)  # Uncomment if you want to rename
