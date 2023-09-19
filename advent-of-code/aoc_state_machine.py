from dataclasses import dataclass


@dataclass
class StateMachine:
    memory: dict[str, int]
    program: list[str]

    def run(self):
        """Run the program"""
        current_line = 0
        while current_line < len(self.program):
            instruction = self.program[current_line]

            # Set a register to a value
            if instruction.startswith("set "):
                register, value = instruction[4], int(instruction[6:])
                self.memory[register] = value

            # Increase the value in a register by 1
            elif instruction.startswith("inc "):
                register = instruction[4]
                self.memory[register] += 1

            # Move the line pointer
            current_line += 1
