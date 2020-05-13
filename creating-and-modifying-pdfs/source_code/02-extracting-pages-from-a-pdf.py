# -----------------------------
# Using the PdfFileWriter Class
# -----------------------------

from PyPDF2 import PdfFileWriter

pdf_writer = PdfFileWriter()

page = pdf_writer.addBlankPage(width=72, height=72)

print(type(page))

from pathlib import Path  # noqa

with Path("blank.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)


# -----------------------------------
# Extracting a Single Page From a PDF
# -----------------------------------

from pathlib import Path  # noqa
from PyPDF2 import PdfFileReader, PdfFileWriter  # noqa

# Change the path to work on your computer if necessary
pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "Pride_and_Prejudice.pdf"
)
input_pdf = PdfFileReader(str(pdf_path))

first_page = input_pdf.getPage(0)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)

with Path("first_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)


# ------------------------------------
# Extracting Multiple Pages From a PDF
# ------------------------------------

from PyPDF2 import PdfFileReader, PdfFileWriter  # noqa
from pathlib import Path  # noqa

pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "Pride_and_Prejudice.pdf"
)
input_pdf = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()
for n in range(1, 4):
    page = input_pdf.getPage(n)
    pdf_writer.addPage(page)

print(pdf_writer.getNumPages())

pdf_writer = PdfFileWriter()

for page in input_pdf.pages[1:4]:
    pdf_writer.addPage(page)

with Path("chapter1_slice.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
