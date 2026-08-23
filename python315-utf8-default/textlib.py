import io


def read_text(path, encoding=None):
    encoding = io.text_encoding(encoding)  # Points at the caller
    with open(path, encoding=encoding) as f:
        return f.read()
