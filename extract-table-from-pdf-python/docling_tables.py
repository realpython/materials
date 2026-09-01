"""Inspect and export tables from a Docling parse result."""

from pathlib import Path

from docling.document_converter import DocumentConverter

PDF_PATH = Path("sample_report.pdf")


def main() -> None:
    document = DocumentConverter().convert(PDF_PATH).document

    print(f"Tables found: {len(document.tables)}\n")

    for index, table in enumerate(document.tables):
        pages = sorted({prov.page_no for prov in table.prov})
        frame = table.export_to_dataframe(doc=document)
        print(f"Table {index}: pages {pages}, shape {frame.shape}")

    index_table = document.tables[0].export_to_dataframe(doc=document)
    print("\nFinancial statement index (table 0):")
    print(index_table.to_string(index=False), end="\n\n")

    operations_table = document.tables[1].export_to_dataframe(doc=document)
    print("Operations statement preview (table 1, first 4 rows):")
    print(operations_table.head(4).to_string())


if __name__ == "__main__":
    main()
