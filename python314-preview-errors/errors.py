import sys
import textwrap

MAX_WIDTH = 80


def main() -> None:
    for title, snippets in get_scenarios().items():
        print_headline(title)
        for snippet in snippets:
            execute(snippet)


def get_scenarios() -> dict[str, list[str]]:
    return {
        "Keyword Typos": [
            "forr i in range(5):",
            "why True:",
        ],
        "Strict elif After else": [
            """
                if x > 0:
                    print("positive")
                else:
                    print("not positive")
                elif x == 0:  # This is invalid
                    print("zero")
            """,
        ],
        "Conditional Expressions": ["1 if True else pass"],
        "String Closures": [
            'message = "She said "Hello" to everyone"',
        ],
        "String Prefix Combinations": ['text = fb"Binary {text}"'],
        "Unpacking Assignments": [
            'dog, age, city, hobbies = ["Frieda", 8, "Berlin"]',
            'dog, age = ["Frieda", 8, "Berlin"]',
        ],
        "Aliases": ["import sys as [alias]"],
        "Unhashable Types": ['grid = {[0, 0]: "Label", [0, 1]: "Input"}'],
        "Math Domain": [
            """
                import math
                math.sqrt(-1)
            """
        ],
        "Context Managers": [
            """
                import asyncio
                async def process_data():
                    with asyncio.TaskGroup() as tg:
                        pass
                
                asyncio.run(process_data())
            """,
            """
                import asyncio
                async def read_file():
                    async with open(__file__) as f:
                        return f.read()
                        
                asyncio.run(read_file())
            """,
        ],
    }


def print_headline(text: str, width: int = MAX_WIDTH) -> None:
    print(f" {text} ".center(width, "="))


def execute(source_code: str) -> None:
    raw_source_code = dedent(source_code)
    try:
        print(with_repl_prompts(raw_source_code))
        exec(raw_source_code, globals())
    except (SyntaxError, ValueError, TypeError) as e:
        sys.excepthook(type(e), e, e.__traceback__)
    finally:
        print()


def with_repl_prompts(source_code: str) -> str:
    return "\n".join(
        (">>> " if i == 0 else "... ") + line
        for i, line in enumerate(source_code.splitlines())
    )


def dedent(source_code: str) -> str:
    return textwrap.dedent(source_code).strip("\n")


if __name__ == "__main__":
    main()
