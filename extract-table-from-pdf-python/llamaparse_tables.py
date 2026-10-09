"""Find HTML tables in a LlamaParse Markdown response and print them."""

import os
import re
from pathlib import Path

from llama_cloud import LlamaCloud

PDF_PATH = Path("sample_report.pdf")
TABLE_PATTERN = re.compile(r"<table\b.*?</table>", re.DOTALL | re.IGNORECASE)


def main() -> None:
    client = LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])

    uploaded = client.files.create(file=PDF_PATH, purpose="parse")
    result = client.parsing.parse(
        file_id=uploaded.id,
        tier="agentic",
        version="latest",
        expand=["markdown"],
    )

    tables = []
    for page_no, page in enumerate(result.markdown.pages, start=1):
        for table_html in TABLE_PATTERN.findall(page.markdown):
            tables.append((page_no, table_html))

    print(f"Tables found: {len(tables)}\n")
    for index, (page_no, table_html) in enumerate(tables):
        print(f"Table {index}: page {page_no}")

    print("\nTable 0:")
    print(tables[0][1], end="\n\n")

    print("Table 1 (truncated):")
    print(tables[1][1][:700], "...")


if __name__ == "__main__":
    main()
