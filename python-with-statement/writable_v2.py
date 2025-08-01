from contextlib import contextmanager


@contextmanager
def writable_file(file_path):
    try:
        file = open(file_path, mode="w")
        yield file
    finally:
        file.close()


if __name__ == "__main__":
    with writable_file("hello.txt") as file:
        file.write("Hello, World!")
