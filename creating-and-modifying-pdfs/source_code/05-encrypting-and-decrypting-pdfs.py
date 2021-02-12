# ---------------
# Encrypting PDFs
# ---------------

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "newsletter.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()
pdf_writer.appendPagesFromReader(pdf_reader)

pdf_writer.encrypt(user_pwd="SuperSecret")

output_path = Path.home() / "newsletter_protected.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)

user_pwd = "SuperSecret"
owner_pwd = "ReallySuperSecret"
pdf_writer.encrypt(user_pwd=user_pwd, owner_pwd=owner_pwd)


# ---------------
# Decrypting PDFs
# ---------------

from pathlib import Path  # noqa
from PyPDF2 import PdfFileReader, PdfFileWriter  # noqa

pdf_path = Path.home() / "newsletter_protected.pdf"

pdf_reader = PdfFileReader(str(pdf_path))

print(pdf_reader.getPage(0))  # Raises PdfReadError

print(pdf_reader.decrypt(password="SuperSecret"))

print(pdf_reader.getPage(0))
