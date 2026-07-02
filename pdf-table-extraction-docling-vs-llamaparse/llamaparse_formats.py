"""Export LlamaParse results to Markdown, Text, and schema-driven JSON."""

import json
import os
from pathlib import Path

from llama_cloud import LlamaCloud
from pydantic import BaseModel, Field

PDF_PATH = Path("sample_report.pdf")


class RevenueRow(BaseModel):
    quarter: str = Field(
        description="Fiscal quarter label, e.g. Q1 2024",
    )
    revenue_millions: float = Field(
        description="Revenue in millions of USD",
    )
    growth_percent: float | None = Field(
        default=None,
        description="Year-over-year growth percentage if stated",
    )

class RevenueTable(BaseModel):
    rows: list[RevenueRow] = Field(
        description="One row per quarter in the table"
    )


def main() -> None:
    client = LlamaCloud(api_key=os.environ["LLAMA_CLOUD_API_KEY"])

    uploaded = client.files.create(file=PDF_PATH, purpose="parse")

    parsed = client.parsing.parse(
        file_id=uploaded.id,
        tier="agentic",
        version="latest",
        expand=["markdown", "text"],
    )

    markdown_pages = "\n\n".join(
        page.markdown for page in parsed.markdown.pages
    )
    Path("output_llamaparse.md").write_text(
        markdown_pages, encoding="utf-8"
    )

    if parsed.text and parsed.text.pages:
        text_pages = "\n".join(
            page.text for page in parsed.text.pages
        )
        Path("output_llamaparse.text").write_text(
            text_pages, encoding="utf-8"
        )

    extract_file = client.files.create(
        file=PDF_PATH, purpose="extract"
    )
    job = client.extract.run(
        file_input=extract_file.id,
        configuration={
            "data_schema": RevenueTable.model_json_schema(),
            "extraction_target": "per_doc",
            "tier": "agentic",
        },
    )

    Path("output_llamaparse.json").write_text(
        json.dumps(job.extract_result, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(job.extract_result, indent=2))


if __name__ == "__main__":
    main()
