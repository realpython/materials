from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class Item:
    name: str
    children: list[Item] = None
    junk_files: int = None


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
                            [Item("2", junk_files=300)],
                            junk_files=300,
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
                                Item("logs", junk_files=300),
                                Item("temp", junk_files=300),
                            ],
                            junk_files=25,
                        ),
                        Item("33.txt"),
                        Item("34.txt"),
                        Item("36.txt"),
                        Item("37.txt"),
                        Item("real_python.txt"),
                    ],
                ),
            ],
            junk_files=5,
        ),
        Item("temp", junk_files=300),
        Item("temporary_files", junk_files=300),
    ],
)


def create_item(item: Item, path_to: Path = Path("")):

    if item.children is None and item.junk_files is None:
        path_to.joinpath(item.name).touch()

    if item.children or item.junk_files:
        root = path_to.joinpath(item.name)
        root.mkdir()

    if item.children:
        for child in item.children:
            create_item(child, path_to=root)

    if item.junk_files:
        for i in range(item.junk_files):
            root.joinpath(f"{i}.txt").touch()


create_item(folder_structure)
