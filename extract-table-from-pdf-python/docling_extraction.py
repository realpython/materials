"""Parse a PDF with Docling and print Markdown output."""

from pathlib import Path

from docling.document_converter import DocumentConverter

PDF_PATH = Path("sample_report.pdf")


def main() -> None:
    converter = DocumentConverter()
    result = converter.convert(PDF_PATH)

    markdown = result.document.export_to_markdown()
    print(markdown[:3000])
    print("\n---\n")
    print(f"Pages parsed: {len(result.document.pages)}")
    print(f"Tables found: {len(result.document.tables)}")


if __name__ == "__main__":
    main()
