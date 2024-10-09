import ast
import sys
import traceback

PROMPT = "\N{snake} "
COMMANDS = ("help", "exit", "quit")


def main():
    print('Type "help" for more information, "exit" or "quit" to finish.')
    while True:
        try:
            match input(PROMPT):
                case command if command.lower() in COMMANDS:
                    match command.lower():
                        case "help":
                            print(f"Python {sys.version}")
                        case "exit" | "quit":
                            break
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
        except EOFError:
            print()
            exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)


def valid(code, mode):
    try:
        ast.parse(code, mode=mode)
        return True
    except SyntaxError:
        return False


if __name__ == "__main__":
    main()
