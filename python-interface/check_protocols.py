from readers_protocols import FileReaderProtocol, PdfReader, EmailReader


def read(reader: FileReaderProtocol, path: str) -> str:
    reader.load_file(path)
    return reader.extract_text()


# Accepted by the type checker
read(PdfReader(), "/reports/report.pdf")
read(EmailReader(), "/mail/message.eml")
