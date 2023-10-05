from typing import Required, TypedDict, Unpack


class Options(TypedDict, total=False):
    line_width: int
    level: Required[str]
    propagate: bool


def show_options(program_name: str, **kwargs: Unpack[Options]) -> None:
    print(program_name.upper())
    for option, value in kwargs.items():
        print(f"{option:<15} {value}")


def show_options_explicit(
    program_name: str,
    *,
    level: str,
    line_width: int | None = None,
    propagate: bool | None = None,
) -> None:
    options = {
        "line_width": line_width,
        "level": level,
        "propagate": propagate,
    }
    print(program_name.upper())
    for option, value in options.items():
        if value is not None:
            print(f"{option:<15} {value}")


show_options("logger", line_width=80, level="INFO", propagate=False)
