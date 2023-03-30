from pathlib import Path
from zipfile import ZipFile

# Bad example
# class FileManager:
#     def __init__(self, filename):
#         self.filename = Path(filename)

#     def read(self):
#         with self.filename.open(mode="r") as file:
#             data = file.read()
#         return data

#     def write(self, data):
#         with self.filename.open(mode="w") as file:
#             file.write(data)

#     def compress(self):
#         with ZipFile(self.filename.stem + ".zip", mode="w") as archive:
#             archive.write(self.filename)

#     def decompress(self, archive_name):
#         with ZipFile(archive_name, mode="r") as archive:
#             archive.extractall()


# Good example
class FileManager:
    def __init__(self, filename):
        self.filename = Path(filename)

    def read(self):
        with self.filename.open(mode="r") as file:
            data = file.read()
        return data

    def write(self, data):
        with self.filename.open(mode="w") as file:
            file.write(data)


class ZipFileArchiver:
    def __init__(self, filename):
        self.filename = Path(filename)

    def compress(self):
        with ZipFile(self.filename.stem + ".zip", mode="w") as archive:
            archive.write(self.filename)

    def decompress(self, archive_name):
        with ZipFile(archive_name, mode="r") as archive:
            archive.extractall()
