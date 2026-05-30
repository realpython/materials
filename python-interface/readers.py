class PdfReader:
    """Extract text from a PDF."""

    def load_file(self, path: str) -> None:
        print(f"Loading PDF from {path}")

    def extract_text(self) -> str:
        return "Extracted PDF text"


class EmailReader:
    """Extract text from an email."""

    def load_file(self, path: str) -> None:
        print(f"Loading email from {path}")

    def extract_text(self) -> str:
        return "Extracted email text"


def read(reader, path: str) -> str:
    reader.load_file(path)
    return reader.extract_text()


print(read(PdfReader(), "/reports/report.pdf"))
print(read(EmailReader(), "/mail/message.eml"))

# class EmailReader:
#     """Extract text from an email."""
#
#     def load_file(self, path: str) -> None:
#         print(f"Loading email from {path}")
#
#     def extract_email_text(self) -> str:
#         return "Extracted email text"
