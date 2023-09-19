# --------------
# Rotating Pages
# --------------

from pathlib import Path

from pypdf import PdfReader, PdfWriter

pdf_path = (
    Path.home() / "creating-and-modifying-pdfs" / "practice_files" / "ugly.pdf"
)

pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()

for i, page in enumerate(pdf_reader.pages):
    if i % 2 == 0:
        page.rotate(90)
    pdf_writer.add_page(page)

pdf_writer.write("ugly_rotated.pdf")

pdf_reader = PdfReader(pdf_path)

first_page = pdf_reader.pages[0]
print(first_page.rotation)

second_page = pdf_reader.pages[1]
print(second_page.rotation)

pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()

for page in pdf_reader.pages:
    if page.rotation != 0:
        page.rotate(-page.rotation)
    pdf_writer.add_page(page)

pdf_writer.write("ugly_rotated2.pdf")

# --------------
# Cropping Pages
# --------------

from pathlib import Path  # noqa

from pypdf import PdfReader, PdfWriter  # noqa

pdf_path = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "half_and_half.pdf"
)

pdf_reader = PdfReader(pdf_path)
first_page = pdf_reader.pages[0]

print(first_page.mediabox)
print(first_page.mediabox.lower_left)
print(first_page.mediabox.lower_right)
print(first_page.mediabox.upper_left)
print(first_page.mediabox.upper_right)

print(first_page.mediabox.upper_right[0])
print(first_page.mediabox.upper_right[1])

first_page.mediabox.upper_left = [0, 480]
print(first_page.mediabox.upper_left)
print(first_page.mediabox.upper_right)

pdf_writer = PdfWriter()
pdf_writer.add_page(first_page)
pdf_writer.write("cropped_page.pdf")

pdf_reader = PdfReader(pdf_path)
pdf_writer = PdfWriter()

first_page = pdf_reader.pages[0]

import copy  # noqa

left_side = copy.deepcopy(first_page)
current_coords = left_side.mediabox.upper_right
new_coords = [current_coords[0] / 2, current_coords[1]]
left_side.mediabox.upper_right = new_coords

right_side = copy.deepcopy(first_page)
right_side.mediabox.upper_left = new_coords

pdf_writer.add_page(left_side)
pdf_writer.add_page(right_side)
pdf_writer.write("cropped_pages.pdf")
