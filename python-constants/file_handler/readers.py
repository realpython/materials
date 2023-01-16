# readers.py


class _DefaultReader:
    def read(self, file):
        with open(file, mode="r", encoding="utf-8") as file_obj:
            for line in file_obj:
                print(line)


DEFAULT_READER = _DefaultReader()
