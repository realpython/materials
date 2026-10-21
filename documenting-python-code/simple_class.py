class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""

        print(f"Hello {name}")


if __name__ == "__main__":
    help(SimpleClass)
