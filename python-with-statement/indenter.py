class Indenter:
    def __init__(self, width=2):
        self.indentation = " " * width
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, *_):
        self.level -= 1

    def print(self, text):
        print(self.indentation * self.level + text)


if __name__ == "__main__":
    with Indenter() as indenter:
        indenter.print("<div>")
        with indenter:
            indenter.print("<p>")
            with indenter:
                indenter.print("Hello, World!")
            indenter.print("</p>")
        indenter.print("</div>")
