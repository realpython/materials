class Words(str):
    def __len__(self):
        return len(self.split())


def inspect[S: str](text: S) -> S:
    print(f"'{text.upper()}' has length {len(text)}")
    return text
