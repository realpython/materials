from pathlib import Path

from markitdown import MarkItDown


def main(
    input_dir,
    output_dir="output",
    target_formats=(".docx", ".xlsx", ".pdf"),
):
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    md = MarkItDown()

    for file_path in input_path.rglob("*"):
        if file_path.suffix in target_formats:
            try:
                result = md.convert(file_path)
            except Exception as e:
                print(f"✗ Error converting {file_path.name}: {e}")
                continue

            output_file = (
                output_path / f"{file_path.stem}{file_path.suffix}.md"
            )
            output_file.write_text(result.markdown, encoding="utf-8")
            print(f"✓ Converted {file_path.name} → {output_file.name}")


if __name__ == "__main__":
    main("data", "output")
