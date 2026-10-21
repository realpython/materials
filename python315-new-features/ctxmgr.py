from contextlib import contextmanager

@contextmanager
def logged(label):
    print(f"enter {label}")
    yield
    print(f"exit {label}")

@logged("reading")
def read_lines():
    yield "first"
    yield "second"

for line in read_lines():
    print(line)
