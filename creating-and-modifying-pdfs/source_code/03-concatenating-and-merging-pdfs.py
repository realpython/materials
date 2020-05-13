# -----------------------------
# Using the PdfFileMerger Class
# -----------------------------

from PyPDF2 import PdfFileMerger

pdf_merger = PdfFileMerger()

# ---------------------------------
# Concatenating PDFs With .append()
# ---------------------------------

from pathlib import Path  # noqa

reports_dir = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "expense_reports"
)

for path in reports_dir.glob("*.pdf"):
    print(path.name)

expense_reports = list(reports_dir.glob("*.pdf"))
expense_reports.sort()

for path in expense_reports:
    print(path.name)

for path in expense_reports:
    pdf_merger.append(str(path))

with Path("expense_reports.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)


# --------------------------
# Merging PDFs With .merge()
# --------------------------

from pathlib import Path  # noqa
from PyPDF2 import PdfFileMerger  # noqa

report_dir = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "quarterly_report"
)

report_path = report_dir / "report.pdf"
toc_path = report_dir / "toc.pdf"

pdf_merger = PdfFileMerger()
pdf_merger.append(str(report_path))

pdf_merger.merge(1, str(toc_path))

with Path("full_report.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)
