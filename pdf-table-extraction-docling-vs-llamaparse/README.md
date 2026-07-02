# PDF Table Extraction: Docling vs LlamaParse

This folder contains the code examples for the Real Python tutorial [PDF Table Extraction: Docling vs LlamaParse](https://realpython.com/pdf-table-extraction-docling-vs-llamaparse/).

The scripts parse `sample_report.pdf`, a short financial report with tables, and compare two approaches:

- **[Docling](https://github.com/docling-project/docling)** runs locally and exports structured document data, including tables as pandas DataFrames.
- **[LlamaParse](https://docs.cloud.llamaindex.ai/llamaparse/getting_started)** uses the Llama Cloud API for parsing and schema-driven extraction.

## Files

| File | Description |
|------|-------------|
| `sample_report.pdf` | Sample PDF used by all scripts |
| `docling_extraction.py` | Parse the PDF with Docling and print Markdown output |
| `docling_tables.py` | Inspect detected tables and print selected DataFrames |
| `docling_formats.py` | Export Docling results to Markdown, JSON, HTML, and DataFrames |
| `llamaparse_extraction.py` | Parse the PDF with LlamaParse and print Markdown output |
| `llamaparse_formats.py` | Export LlamaParse results to Markdown, plain text, and JSON |
| `requirements.txt` | Pinned dependencies for this folder |

## Installation

Create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/), then install the dependencies:

```shell
$ python3 -m venv venv/
$ source venv/bin/activate
(venv) $ python -m pip install -r requirements.txt
```

Run the scripts from this folder so the relative path to `sample_report.pdf` resolves correctly.

## Docling examples

Docling runs on your machine and does not require an API key.

```shell
(venv) $ python docling_extraction.py
(venv) $ python docling_tables.py
(venv) $ python docling_formats.py
```

`docling_formats.py` writes `output_docling.md`, `output_docling.json`, and `output_docling.html` in the current directory.

## LlamaParse examples

The LlamaParse scripts require a [Llama Cloud API key](https://cloud.llamaindex.ai/). Export it before running:

```shell
(venv) $ export LLAMA_CLOUD_API_KEY="your-api-key"
(venv) $ python llamaparse_extraction.py
(venv) $ python llamaparse_formats.py
```

`llamaparse_formats.py` writes `output_llamaparse.md`, `output_llamaparse.text`, and `output_llamaparse.json` in the current directory.
