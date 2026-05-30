from typing import Protocol, runtime_checkable


@runtime_checkable
class FileReaderProtocol(Protocol):
    """Protocol for file readers."""

    def load_file(self, path: str) -> None:
        """Load a file for text extraction."""
        ...

    def extract_text(self) -> str:
        """Return text extracted from the loaded file."""
        ...


class PdfReader:
    """Extract text from a PDF."""

    def load_file(self, path: str) -> None:
        """Load a PDF file for text extraction."""
        print(f"Loading PDF from {path}")

    def extract_text(self) -> str:
        """Return text extracted from the loaded PDF."""
        return "Extracted PDF text"


class EmailReader:
    """Extract text from an Email."""

    def load_file(self, path: str) -> None:
        """Load an EML file for text extraction."""
        print(f"Loading email from {path}")

    def extract_text(self) -> str:
        """Return text extracted from the loaded email."""
        return "Extracted email text"
