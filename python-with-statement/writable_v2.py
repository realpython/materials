from contextlib import contextmanager


@contextmanager
def writable_file(file_path):
    file = open(file_path, mode="w")
    yield file
    file.close()


with writable_file("hello.txt") as file:
    file.write("Hello, World!")
