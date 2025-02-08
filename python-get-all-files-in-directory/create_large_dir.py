from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

NUM_JUNK_FILES_LARGE = 300
NUM_JUNK_FILES_MEDIUM = 25
NUM_JUNK_FILES_SMALL = 5


@dataclass
class Item:
    name: str
    children: list[Item] = field(default_factory=list)
    num_junk_files: int = 0


folder_structure = Item(
    "large_dir",
    [
        Item(
            "documents",
            [
                Item(
                    "notes",
                    [
                        Item(
                            "temp",
                            [Item("2", num_junk_files=NUM_JUNK_FILES_LARGE)],
                            num_junk_files=NUM_JUNK_FILES_LARGE,
                        ),
                        Item("0.txt"),
                        Item("find_me.txt"),
                    ],
                ),
                Item(
                    "tools",
                    [
                        Item(
                            "temporary_files",
                            [
                                Item(
                                    "logs", num_junk_files=NUM_JUNK_FILES_LARGE
                                ),
                                Item(
                                    "temp", num_junk_files=NUM_JUNK_FILES_LARGE
                                ),
                            ],
                            num_junk_files=NUM_JUNK_FILES_MEDIUM,
                        ),
                        Item("33.txt"),
                        Item("34.txt"),
                        Item("36.txt"),
                        Item("37.txt"),
                        Item("real_python.txt"),
                    ],
                ),
            ],
            num_junk_files=NUM_JUNK_FILES_SMALL,
        ),
        Item("temp", num_junk_files=NUM_JUNK_FILES_LARGE),
        Item("temporary_files", num_junk_files=NUM_JUNK_FILES_LARGE),
    ],
)


def create_item(item: Item, path_to: Path = Path.cwd()) -> None:

    if not item.children and not item.num_junk_files:
        path_to.joinpath(item.name).touch(exist_ok=True)
        return

    root = path_to.joinpath(item.name)
    root.mkdir(exist_ok=True)

    for child in item.children:
        create_item(child, path_to=root)

    for i in range(item.num_junk_files):
        root.joinpath(f"{i}.txt").touch(exist_ok=True)


create_item(folder_structure)
