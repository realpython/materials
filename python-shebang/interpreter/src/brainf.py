import fileinput
import sys


def main() -> None:
    with fileinput.input(encoding="utf-8") as file:
        interpret("".join(line for line in file if not line.startswith("#")))


def interpret(code: str, memory_size: int = 2**15) -> None:
    memory, jumps = [0] * memory_size, find_matching_brackets(code)
    ip = ptr = 0
    while ip < len(code):
        match code[ip]:
            case ">":
                ptr += 1
            case "<":
                ptr -= 1
            case "+":
                memory[ptr] += 1
            case "-":
                memory[ptr] -= 1
            case ".":
                print(chr(memory[ptr]), end="")
            case ",":
                memory[ptr] = ord(c) if (c := sys.stdin.read(1)) else 0
            case "[":
                if memory[ptr] == 0:
                    ip = jumps[ip]
            case "]":
                if memory[ptr] != 0:
                    ip = jumps[ip]
        ip += 1


def find_matching_brackets(code: str) -> dict[int, int]:
    jumps, stack = {}, []
    for i, instruction in enumerate(code):
        if instruction == "[":
            stack.append(i)
        elif instruction == "]":
            jumps[i], jumps[j] = (j := stack.pop()), i
    return jumps


if __name__ == "__main__":
    main()
