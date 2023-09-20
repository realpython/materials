from typing import TypeVar

S = TypeVar("S", bound=str)


class Words(str):
    def __len__(self):
        return len(self.split())


def inspect(text: S) -> S:
    print(f"'{text.upper()}' has length {len(text)}")
    return text


# %% Python 3.12

# class Words(str):
#     def __len__(self):
#         return len(self.split())
#
#
# def inspect[S: str](text: S) -> S:
#     print(f"'{text.upper()}' has length {len(text)}")
#     return text
