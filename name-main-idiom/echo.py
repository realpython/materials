def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoes = [text[-i:].lower() for i in range(repetitions, 0, -1)]
    return "\n".join(echoes + ["."])


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
