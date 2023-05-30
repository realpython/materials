# ---------------
# Encrypting PDFs
# ---------------

from pathlib import Path

from pypdf import PdfReader, PdfWriter

pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "newsletter.pdf"
)

pdf_reader = PdfReader(pdf_path)

pdf_writer = PdfWriter()
pdf_writer.append_pages_from_reader(pdf_reader)

pdf_writer.encrypt(user_password="SuperSecret")

output_path = Path.home() / "newsletter_protected.pdf"
pdf_writer.write(output_path)

user_pwd = "SuperSecret"
owner_pwd = "ReallySuperSecret"
pdf_writer.encrypt(user_password=user_pwd, owner_password=owner_pwd)


# ---------------
# Decrypting PDFs
# ---------------

from pathlib import Path  # noqa

from pypdf import PdfReader  # noqa

pdf_path = Path.home() / "newsletter_protected.pdf"

pdf_reader = PdfReader(pdf_path)

print(pdf_reader.pages[0])  # Raises FileNotDecryptedError

print(pdf_reader.decrypt(password="SuperSecret"))

print(pdf_reader.pages[0])
