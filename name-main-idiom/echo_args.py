import sys


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoes = [text[-i:].lower() for i in range(repetitions, 0, -1)]
    return "\n".join(echoes + ["."])


def main() -> None:
    text = " ".join(sys.argv[1:])
    print(echo(text))


if __name__ == "__main__":
    main()
