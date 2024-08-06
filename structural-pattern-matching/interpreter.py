import sys


def interpret(code, num_bytes=2**10):
    stack, brackets = [], {}
    for i, instruction in enumerate(code):
        match instruction:
            case "[":
                stack.append(i)
            case "]":
                brackets[i], brackets[j] = (j := stack.pop()), i
    memory = bytearray(num_bytes)
    pointer = ip = 0
    while ip < len(code):
        match code[ip]:
            case ">":
                pointer += 1
            case "<":
                pointer -= 1
            case "+":
                memory[pointer] += 1
            case "-":
                memory[pointer] -= 1
            case ".":
                print(chr(memory[pointer]), end="")
            case ",":
                memory[pointer] = ord(sys.stdin.buffer.read(1))
            case "[" if memory[pointer] == 0:
                ip = brackets[ip]
            case "]" if memory[pointer] != 0:
                ip = brackets[ip]
        ip += 1


if __name__ == "__main__":
    interpret(
        """
      +++++++++++[>++++++>+++++++++>++++++++>++++>+++>+<<<<<<-]>+++
      +++.>++.+++++++..+++.>>.>-.<<-.<.+++.------.--------.>>>+.>-.
    """
    )
