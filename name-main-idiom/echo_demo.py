def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."


if __name__ == "__main__":
    print("Example call: echo('HELLO', repetitions=2)", end=f"\n{'-'*40}\n")
    print(echo("HELLO", repetitions=2))
