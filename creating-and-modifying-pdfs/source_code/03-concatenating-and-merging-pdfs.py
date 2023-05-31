# -----------------------------
# Using the PdfFileMerger Class
# -----------------------------

from pypdf import PdfMerger

pdf_merger = PdfMerger()

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

expense_reports = sorted(reports_dir.glob("*.pdf"))

for path in expense_reports:
    print(path.name)

pdf_merger = PdfMerger()

for path in expense_reports:
    pdf_merger.append(path)

pdf_merger.write("expense_reports.pdf")


# --------------------------
# Merging PDFs With .merge()
# --------------------------

from pathlib import Path  # noqa

from pypdf import PdfMerger  # noqa

report_dir = (
    Path.home()
    / "creating-and-modifying-pdfs"
    / "practice_files"
    / "quarterly_report"
)

report_path = report_dir / "report.pdf"
toc_path = report_dir / "toc.pdf"

pdf_merger = PdfMerger()
pdf_merger.append(report_path)

pdf_merger.merge(1, toc_path)

pdf_merger.write("full_report.pdf")
