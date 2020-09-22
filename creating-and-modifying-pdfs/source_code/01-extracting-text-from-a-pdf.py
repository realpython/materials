# ---------------
# Open a PDF File
# ---------------

from PyPDF2 import PdfFileReader

# You might need to change this to match the path on your computer
from pathlib import Path

pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "Pride_and_Prejudice.pdf"
)

pdf = PdfFileReader(str(pdf_path))

print(pdf.getNumPages())

print(pdf.documentInfo)

print(pdf.documentInfo.title)


# ---------------------------
# Extracting Text From a Page
# ---------------------------

first_page = pdf.getPage(0)

print(type(first_page))

print(first_page.extractText())

for page in pdf.pages:
    print(page.extractText())


# -----------------------
# Putting It All Together
# -----------------------

from pathlib import Path  # noqa
from PyPDF2 import PdfFileReader  # noqa

# Change the path below to the correct path for your computer.
pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice-files"
    / "Pride_and_Prejudice.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
output_file_path = Path.home() / "Pride_and_Prejudice.txt"

with output_file_path.open(mode="w") as output_file:
    title = pdf_reader.documentInfo.title
    num_pages = pdf_reader.getNumPages()
    output_file.write(f"{title}\\nNumber of pages: {num_pages}\\n\\n")

    for page in pdf_reader.pages:
        text = page.extractText()
        output_file.write(text)
