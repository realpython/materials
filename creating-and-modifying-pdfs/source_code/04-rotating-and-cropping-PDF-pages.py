# --------------
# Rotating Pages
# --------------

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
    Path.home() / "creating-and-modifying-pdfs" / "practice_files" / "ugly.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for n in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(n)
    if n % 2 == 0:
        page.rotateClockwise(90)
    pdf_writer.addPage(page)

with Path("ugly_rotated.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

pdf_reader = PdfFileReader(str(pdf_path))

print(pdf_reader.getPage(0))

page = pdf_reader.getPage(0)
print(page["/Rotate"])

page = pdf_reader.getPage(1)
print(page["/Rotate"])

page = pdf_reader.getPage(0)
print(page["/Rotate"])

page.rotateClockwise(90)
print(page["/Rotate"])

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    if page["/Rotate"] == -90:
        page.rotateClockwise(90)
    pdf_writer.addPage(page)

with Path("ugly_rotated2.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)


# --------------
# Cropping Pages
# --------------

from pathlib import Path  # noqa
from PyPDF2 import PdfFileReader, PdfFileWriter  # noqa

pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "half_and_half.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
first_page = pdf_reader.getPage(0)

print(first_page.mediaBox)
print(first_page.mediaBox.lowerLeft)
print(first_page.mediaBox.lowerRight)
print(first_page.mediaBox.upperLeft)
print(first_page.mediaBox.upperRight)
print(first_page.mediaBox.upperRight[0])
print(first_page.mediaBox.upperRight[1])

first_page.mediaBox.upperLeft = (0, 480)
print(first_page.mediaBox.upperLeft)
print(first_page.mediaBox.upperRight)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)
with Path("cropped_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

first_page = pdf_reader.getPage(0)

import copy  # noqa

left_side = copy.deepcopy(first_page)
current_coords = left_side.mediaBox.upperRight
new_coords = (current_coords[0] / 2, current_coords[1])
left_side.mediaBox.upperRight = new_coords

right_side = copy.deepcopy(first_page)
right_side.mediaBox.upperLeft = new_coords

pdf_writer.addPage(left_side)
pdf_writer.addPage(right_side)
with Path("cropped_pages.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
