# AOC 2022 Day 07

import pathlib

root_path = pathlib.Path.home() / "git" / "AOC2022" / "day07" / "day07"


def get_path_name(folder_name):
    if len(folder_name) > 1:
        return "/".join(folder_name)[1:]
    else:
        return "/".join(folder_name)


def parse(lines):

    # We read each line and create some structures
    # - We maintain a path list stack, which tells us how deep the structure is
    #   - It starts with ["/"]
    #   - We can do a "/".join(path)[1:] to get the full path, and drop the "/"
    # - We maintain a dictionary of paths to files
    #   - The key is the full path
    #   - The value is a list of tuples
    #     - Each tuple contains the name and file size
    #
    # Here's the plan when we get to each line
    # - if it's a cd command
    #   - If it's a directory name, we push that onto the end of the path list
    #   - If it's a .., we pop the last item off the path list
    # - if it's an ls command, or a dir <name>
    #   - skip to the next line
    # - if it's a number and file
    #   - construct the tuple (file, size)
    #   - Get the full path with the code above
    #     - Is this path in the dictionary?
    #       - If not, create it with a blank list
    #   - Append the tuple to the path list

    # Where do we keep the folder names
    folder_name = ["/"]

    # Where do we keep the files and sizes
    folder_files = {}

    # Start reading at the second line - we know the first two line
    for line in lines[2:]:
        # Split the line so we can parse it
        part = line.split()

        # What kind of line is it?
        # Are we changing into a folder
        if part[1] == "ls":
            # We can skip these lines
            continue

        # Is it a folder? We need to ready for it
        if part[0] == "dir":
            # Get the current path, and append this path to it
            path = get_path_name(folder_name)
            if path.endswith("/"):
                path += part[1]
            else:
                path += "/" + part[1]

            # Add a blank to the dictionary
            # If we don't do this, we miss empty folders in our output
            # They may contribute to the answer later.
            folder_files[path] = []

            # Keep going
            continue

        # Are we changing folders
        if part[1] == "cd":
            # Backing up? Remove this folder
            if part[2] == "..":
                folder_name.pop()
            # Heading down? Add this folder
            else:
                folder_name.append(part[2])

        else:
            # It's a file, so we need the full path
            path = get_path_name(folder_name)

            if path not in folder_files.keys():
                folder_files[path] = []

            # Append this tuple to that list
            folder_files[path].append((part[1], int(part[0])))

    # We're done, return the dictionary
    return folder_files


def get_file_sizes(tree):

    # We've got the tree, so we need all the keys
    paths = sorted([k for k in tree.keys()], reverse=True)

    # We need a dictionary to store the file sizes for each path
    files_sizes = {}

    # And a place for the total
    for current_path in paths:
        for containing_path in tree.keys():
            if containing_path.startswith(current_path):
                # Do we have a current path
                if current_path not in files_sizes.keys():
                    files_sizes[current_path] = 0

                # Add the files in this folder
                for _, size in tree[containing_path]:
                    files_sizes[current_path] += size

                # print(f"Checking {check_path}... {current_path} is in it")

    # DEBUG: Print the files sizes
    # for k, v in files_sizes.items():
    #     print(f"Folder {k} contains {v} bytes of files")
    return files_sizes


def part1(file_sizes):

    total = 0

    # Now we can go through them all in this order
    for _, total_size in file_sizes.items():
        if total_size <= 100_000:
            total += total_size

    return total


def part2(file_sizes):
    # How much free space do we have?
    free_space = 70_000_000 - file_sizes["/"]

    # How much more do we need?
    needed_space = 30_000_000 - free_space

    # Let's find the one folder which gets us to enough free space
    space = 70_000_000
    for _, proposed in file_sizes.items():
        # Not enough space?
        if proposed < needed_space:
            continue

        # Found one, let's make sure it's the smallest
        space = min(space, proposed)

    return space


if __name__ == "__main__":

    with open(root_path / "input", "r") as f:
        # with open(root_path / "sample", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    tree = parse(lines)
    file_sizes = get_file_sizes(tree)

    print(f"Part 1: Answer: {part1(file_sizes)}")
    print(f"Part 2: Answer: {part2(file_sizes)}")
