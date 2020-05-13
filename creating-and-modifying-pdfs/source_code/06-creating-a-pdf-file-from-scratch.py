# ----------------------
# Using the Canvas Class
# ----------------------

from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("hello.pdf")
canvas.drawString(72, 72, "Hello, World")
canvas.save()


# ---------------------
# Setting the Page Size
# ---------------------

from reportlab.lib.units import inch, cm

print(cm)
print(inch)

canvas = Canvas("hello.pdf", pagesize=(8.5 * inch, 11 * inch))

from reportlab.lib.pagesizes import LETTER

canvas = Canvas("hello.pdf", pagesize=LETTER)
print(LETTER)


# -----------------------
# Setting Font Properties
# -----------------------

canvas = Canvas("font-example.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 18)
canvas.drawString(1 * inch, 10 * inch, "Times New Roman (18 pt)")
canvas.save()

# The code below creates a PDF with blue text
from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("font-colors.pdf", pagesize=LETTER)

# Set font to Times New Roman with 12-point size
canvas.setFont("Times-Roman", 12)

# Draw blue text one inch from the left and ten
# inches from the bottom
canvas.setFillColor(blue)
canvas.drawString(1 * inch, 10 * inch, "Blue text")

# Save the PDF file
canvas.save()
