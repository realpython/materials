import pathlib
from pprint import pp

import skip_dirs  # See skip_dirs.py for details

# Create a Path object
desktop = pathlib.Path("Desktop")

############################################
# GETTING A LIST OF FILES AND DIRECTORIES
############################################

# Basic listing using .iterdir()
pp(list(desktop.iterdir()))

# Iteration to filter or process
for item in desktop.iterdir():
    print(f"{item} - {'dir' if item.is_dir() else 'file'}")

# Usage in a comprehension
pp([item for item in desktop.iterdir() if item.is_dir()])

############################################
# RECURSIVELY LIST WITH GLOBS
############################################

# Recursively list with glob (both lines are equivalent)
pp(list(desktop.rglob("*")))
pp(list(desktop.glob("**/*")))

############################################
# CONDITIONAL LISTING WITH GLOBS
############################################

# Conditional listing using glob patterns
pp(list(desktop.glob("*")))  # Does not recurse
pp(list(desktop.glob("real*")))
pp(list(desktop.glob("*.txt")))

# Conditional recursive listing
pp(list(desktop.rglob("*.py")))  # Equivalent to .glob("**/*.py")
pp(list(desktop.glob("**/*.py")))  # Equivalent to .rglob("*.py")


# More complex filtering

# With a for loop
for item in desktop.rglob("*"):
    if item.is_file():
        print(item)

# With comprehensions
pp([file for file in desktop.rglob("*") if file.suffix in [".py", ".md"]])
pp([file for file in desktop.rglob("*") if file.is_dir()])

# With the filter() function
pp([list(filter(lambda item: item.is_file(), desktop.rglob("*")))])


############################################
# OPTING OUT OF JUNK DIRECTORIES
############################################

SKIP_DIRS = ["temp", "temporary_files", "logs"]
large_dir = pathlib.Path("large_dir")

# Note: You first find files with .rglob() and then explicitly discard the
# junk directories

# With a for loop
for item in large_dir.rglob("*"):
    if set(item.parts).isdisjoint(SKIP_DIRS):
        print(item)

# With a comprehension
pp(
    [
        item
        for item in large_dir.rglob("*")
        if set(item.parts).isdisjoint(SKIP_DIRS)
    ]
)

# With filter()
pp(
    list(
        filter(
            lambda item: set(item.parts).isdisjoint(SKIP_DIRS),
            large_dir.rglob("*"),
        )
    )
)

############################################
# RECURSIVE ITERDIR
############################################

pp(list(skip_dirs.get_all_items(large_dir)))
