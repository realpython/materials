import ast
import atexit
import readline
import rlcompleter
import sys
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

STANDARD_PROMPT = ">>> "
INDENTED_PROMPT = "... "
TAB_WIDTH = 4
TAB = TAB_WIDTH * " "
COMMANDS = ("help", "exit", "quit")
PYTHON_HISTORY = Path.home() / ".python_history"


@dataclass
class Console:
    indentation_level: int = 0

    def __post_init__(self) -> None:
        readline.parse_and_bind("tab: complete")
        readline.set_completer(rlcompleter.Completer().complete)
        if PYTHON_HISTORY.exists():
            readline.read_history_file(PYTHON_HISTORY)
        atexit.register(readline.write_history_file, PYTHON_HISTORY)

    @property
    def prompt(self) -> str:
        if self.indentation_level > 0:
            return INDENTED_PROMPT
        else:
            return STANDARD_PROMPT

    @property
    def indentation(self) -> str:
        return TAB * self.indentation_level

    def indent(self) -> None:
        self.indentation_level += 1

    def dedent(self) -> None:
        if self.indentation_level > 0:
            self.indentation_level -= 1

    def reindent(self, line: str) -> None:
        num_leading_spaces = len(line) - len(line.lstrip())
        new_indentation_level = num_leading_spaces // TAB_WIDTH
        if new_indentation_level < self.indentation_level:
            self.indentation_level = new_indentation_level

    def input(self) -> str:
        def hook():
            readline.insert_text(self.indentation)
            readline.redisplay()

        try:
            readline.set_pre_input_hook(hook)
            result = input(self.prompt)
            return result
        finally:
            readline.set_pre_input_hook()


@dataclass
class CodeBlock:
    lines: list[str] = field(default_factory=list)

    def execute(self) -> None:
        exec("\n".join(self.lines), globals())
        self.lines = []


def main() -> None:
    print('Type "help" for more information, "exit" or "quit" to finish.')
    console = Console()
    block = CodeBlock()
    while True:
        try:
            match console.input():
                case command if command.lower() in COMMANDS:
                    match command.lower():
                        case "help":
                            print(f"Python {sys.version}")
                        case "exit" | "quit":
                            break
                case line if line.endswith(":"):
                    block.lines.append(line)
                    console.reindent(line)
                    console.indent()
                case line if line.lstrip() == "":
                    console.reindent(line)
                    console.dedent()
                    if console.indentation_level == 0 and block.lines:
                        block.execute()
                case line if console.indentation_level > 0:
                    block.lines.append(line)
                case expression if valid(expression, "eval"):
                    _ = eval(expression)
                    if _ is not None:
                        print(_)
                case statement if valid(statement, "exec"):
                    exec(statement)
                case _:
                    print("Please type a command or valid Python")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
            console.indentation_level = 0
            block.lines = []
        except EOFError:
            print()
            sys.exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)
            console.indentation_level = 0
            block.lines = []


def valid(code: str, mode: Literal["eval", "exec"]) -> bool:
    try:
        ast.parse(code, mode=mode)
        return True
    except SyntaxError:
        return False


if __name__ == "__main__":
    main()
