# file_handler.py

from readers import DEFAULT_READER


class FileHandler:
    def __init__(self, file, reader=DEFAULT_READER):
        self._file = file
        self._reader = reader

    def read(self):
        self._reader.read(self._file)

    # FileHandler implementation goes here...
