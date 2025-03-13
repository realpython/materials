from mmap import ACCESS_READ, mmap
from pathlib import Path
from typing import Iterator, Self


class OpenStreetMap:
    def __init__(self, path: Path) -> None:
        self.file = path.open(mode="rb")
        self.stream = mmap(self.file.fileno(), 0, access=ACCESS_READ)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.stream.close()
        self.file.close()

    def __iter__(self) -> Iterator[bytes]:
        end = 0
        while (begin := self.stream.find(b"<way", end)) != -1:
            end = self.stream.find(b"</way>", begin)
            yield self.stream[begin : end + len(b"</way>")]


if __name__ == "__main__":
    with OpenStreetMap(Path("map.osm")) as osm:
        for way_tag in osm:
            print(way_tag)
