from typing import Protocol


# @runtime_checkable # Uncomment for runtime checks of protocol adherence
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
        print("Loading your PDF...")

    def extract_text(self) -> str:
        """Return text extracted from the loaded PDF."""
        return "Your PDF content"


class EmailReader:
    """Extract text from an Email."""

    def load_file(self, path: str) -> None:
        """Load an EML file for text extraction."""
        print("Loading your Email...")

    def extract_text(self) -> str:
        """Return text extracted from the loaded Email."""
        return "Your Email content"
