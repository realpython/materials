"""A magical module for adding and listing magical characters."""


def add_characters(magical_being):
    """Add a new magical character."""
    return f"You've added {magical_being} to the magical beings record"


if __name__ == "__main__":
    print(add_characters("Gandalf"))
