import sys


class StandardOutputRedirector:
    def __init__(self, new_output):
        self.new_output = new_output

    def __enter__(self):
        self.std_output = sys.stdout
        sys.stdout = self.new_output

    def __exit__(self, *_):
        sys.stdout = self.std_output
