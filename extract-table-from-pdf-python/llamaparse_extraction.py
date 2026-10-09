"""Parse a PDF with LlamaParse (llama-cloud SDK) and print Markdown output."""

import os
from pathlib import Path

from llama_cloud import LlamaCloud

PDF_PATH = Path("sample_report.pdf")


def main() -> None:
    client = LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])

    uploaded = client.files.create(file=PDF_PATH, purpose="parse")
    result = client.parsing.parse(
        file_id=uploaded.id,
        tier="agentic",
        version="latest",
        expand=["markdown"],
    )

    pages = ""
    for page in result.markdown.pages:
        pages += page.markdown
        pages += "\n---\n"

    print(pages[:3000])
    print(f"Pages parsed: {len(result.markdown.pages)}")


if __name__ == "__main__":
    main()
