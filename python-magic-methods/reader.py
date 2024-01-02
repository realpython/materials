class TextFileReader:
    def __init__(self, file_path, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def __enter__(self):
        self.file_obj = open(self.file_path, mode="r", encoding=self.encoding)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()
