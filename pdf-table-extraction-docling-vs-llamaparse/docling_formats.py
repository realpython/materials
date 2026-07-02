"""Export Docling parse results to Markdown, JSON, HTML, and pandas DataFrames."""

import json
from pathlib import Path

from docling.document_converter import DocumentConverter

PDF_PATH = Path("sample_report.pdf")


def main() -> None:
    converter = DocumentConverter()
    document = converter.convert(PDF_PATH).document

    markdown = document.export_to_markdown()
    Path("output_docling.md").write_text(
        markdown, encoding="utf-8"
    )

    payload = document.export_to_dict()
    Path("output_docling.json").write_text(
        json.dumps(payload, indent=2),
        encoding="utf-8",
    )

    html = document.export_to_html()
    Path("output_docling.html").write_text(
        html, encoding="utf-8"
    )

    for index, table in enumerate(document.tables):
        frame = table.export_to_dataframe(doc=document)
        print(f"Table {index} shape: {frame.shape}")
        print(frame.head(), end="\n\n")


if __name__ == "__main__":
    main()
