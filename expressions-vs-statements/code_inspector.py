import ast


def main():
    print("Type a Python code snippet or leave empty to exit.")
    while code := input(">>> "):
        print(describe(code))


def describe(code):
    if valid(code, mode="eval"):
        return "expression"
    elif valid(code, mode="exec"):
        return "statement"
    else:
        return "invalid"


def valid(code, mode):
    try:
        ast.parse(code, mode=mode)
        return True
    except SyntaxError:
        return False


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        pass
