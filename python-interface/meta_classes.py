class ReaderMeta(type):
    """A Reader metaclass used for reader class creation."""

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (
            hasattr(subclass, "load_file")
            and callable(subclass.load_file)
            and hasattr(subclass, "extract_text")
            and callable(subclass.extract_text)
        )


class VirtualFileReader(metaclass=ReaderMeta):
    """Virtual class."""


class PdfReader:
    """Extract text from a PDF."""

    def load_file(self, path: str) -> None:
        print(f"Loading PDF from {path}")

    def extract_text(self) -> str:
        return "Extracted PDF text"


class EmailReader:
    """Extract text from an Email."""

    def load_file(self, path: str) -> None:
        print(f"Loading Email from {path}")

    def extract_email_text(self) -> str:
        return "Extracted Email text"
