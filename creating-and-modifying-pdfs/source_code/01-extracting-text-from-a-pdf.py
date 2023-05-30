# ---------------
# Opening a PDF File
# ---------------

from pathlib import Path

from pypdf import PdfReader

pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "Pride_and_Prejudice.pdf"
)

pdf_reader = PdfReader(pdf_path)

print(len(pdf_reader.pages))

print(pdf_reader.metadata)

print(pdf_reader.metadata.title)


# ---------------------------
# Extracting Text From a Page
# ---------------------------

first_page = pdf_reader.pages[0]

print(type(first_page))

print(first_page.extract_text())

for page in pdf_reader.pages:
    print(page.extract_text())


# -----------------------
# Putting It All Together
# -----------------------

from pathlib import Path  # noqa

from pypdf import PdfReader  # noqa

# Change the path below to the correct path for your computer.
pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "Pride_and_Prejudice.pdf"
)

pdf_reader = PdfReader(pdf_path)
txt_file = Path.home() / "Pride_and_Prejudice.txt"

content = [
    f"{pdf_reader.metadata.title}",
    f"Number of pages: {len(pdf_reader.pages)}",
]

for page in pdf_reader.pages:
    content.append(page.extract_text())

txt_file.write_text("\n".join(content))
