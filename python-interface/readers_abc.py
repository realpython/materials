from abc import ABC, abstractmethod


class FileReaderInterface(ABC):
    """Interface for file readers."""

    @abstractmethod
    def load_file(self, path: str) -> None:
        """Load a file for text extraction."""

    @abstractmethod
    def extract_text(self) -> str:
        """Return text extracted from the loaded file."""


class PdfReader(FileReaderInterface):
    """Extract text from a PDF."""

    def load_file(self, path: str) -> None:
        """Load a PDF file for text extraction."""
        print(f"Loading PDF from {path}")

    def extract_text(self) -> str:
        """Return text extracted from the loaded PDF."""
        return "Extracted PDF text"


class EmailReader(FileReaderInterface):
    """Extract text from an Email."""

    def load_file(self, path: str) -> None:
        """Load an EML file for text extraction."""
        print(f"Loading Email from {path}")

    def extract_email_text(self) -> str:
        """Return text extracted from the loaded Email."""
        return "Extracted Email text"
