from readers_abc import EmailReader, FileReaderInterface, PdfReader

pdf_reader = PdfReader()
email_reader = EmailReader()

print(isinstance(PdfReader(), FileReaderInterface))
print(issubclass(PdfReader, FileReaderInterface))
