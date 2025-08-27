import sys


class StandardOutputRedirector:
    def __init__(self, new_output):
        self.new_output = new_output

    def __enter__(self):
        self.std_output = sys.stdout
        sys.stdout = self.new_output

    def __exit__(self, *_):
        sys.stdout = self.std_output


if __name__ == "__main__":
    with open("hello.txt", "w") as file:
        with StandardOutputRedirector(file):
            print("Hello, World!")
        print("Back to the standard output...")
