from base64 import b64encode
from pathlib import Path


def embed_image(path: Path, label: str = "") -> str:
    ascii_string = b64encode(path.read_bytes()).decode("ascii")
    print(len(path.read_bytes()))
    print(len(ascii_string))
    return f"![{label}](data:image/jpeg;base64,{ascii_string})"


if __name__ == "__main__":
    output_path = Path("picture.md")
    output_path.write_text(embed_image(Path("picture.jpg")))
    print("Saved", output_path)
