from typing import Iterator


def read_chunks(filename: str, max_bytes: int = 1024) -> Iterator[bytes]:
    with open(filename, mode="rb") as file:
        while True:
            chunk = file.read(max_bytes)
            if chunk == b"":
                break
            yield chunk


if __name__ == "__main__":
    for chunk in read_chunks("picture.jpg"):
        print(len(chunk))
