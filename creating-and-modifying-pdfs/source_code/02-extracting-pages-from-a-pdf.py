# -----------------------------
# Using the PdfWriter Class
# -----------------------------

from pypdf import PdfWriter

output_pdf = PdfWriter()

page = output_pdf.add_blank_page(width=8.27 * 72, height=11.7 * 72)

print(type(page))

from pathlib import Path  # noqa

output_pdf.write("blank.pdf")

# -----------------------------------
# Extracting a Single Page From a PDF
# -----------------------------------

from pathlib import Path  # noqa

from pypdf import PdfReader, PdfWriter  # noqa

# Change the path to work on your computer if necessary
pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "Pride_and_Prejudice.pdf"
)
input_pdf = PdfReader(pdf_path)

first_page = input_pdf.pages[0]

output_pdf = PdfWriter()
output_pdf.add_page(first_page)

output_pdf.write("first_page.pdf")


# ------------------------------------
# Extracting Multiple Pages From a PDF
# ------------------------------------

from pathlib import Path  # noqa

from pypdf import PdfReader, PdfWriter  # noqa

pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "Pride_and_Prejudice.pdf"
)
input_pdf = PdfReader(pdf_path)

output_pdf = PdfWriter()

for page in input_pdf.pages[1:4]:
    output_pdf.add_page(page)

print(len(output_pdf.pages))

output_pdf.write("chapter1.pdf")
