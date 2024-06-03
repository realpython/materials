class CommandProcessor:
    def __init__(self):
        self.commands = {}

    def register_command(self, command):
        if not callable(command):
            raise ValueError("command is not callable")
        self.commands[command.__name__] = command

    def execute_command(self, name, *args, **kwargs):
        if (command := self.commands.get(name)) is None:
            raise ValueError(f"command '{name}' not found")
        return command(*args, **kwargs)


def add(a, b):
    return a + b


subtract = 3 - 2


command_processor = CommandProcessor()
command_processor.register_command(add)
command_processor.register_command(subtract)

print(command_processor.execute_command("add", 1, 2))
print(command_processor.register_command(subtract))
