import copy
from datetime import UTC, datetime
from pprint import pp


class ConsoleWindow:
    def __init__(self, tabs):
        self.tabs = tabs
        self.history = []
        self.created_at = datetime.now(UTC)

    def __copy__(self):
        instance = type(self)(self.tabs)
        instance.history = self.history
        self.tabs.add(instance)
        return instance

    def __deepcopy__(self, memo):
        instance = type(self)(self.tabs)
        instance.history = copy.deepcopy(self.history, memo)
        self.tabs.add(instance)
        return instance

    def run_command(self, command):
        self.history.append(command)


if __name__ == "__main__":
    shared_registry = set()
    window = ConsoleWindow(shared_registry)
    window.run_command("cd ~/Projects")
    tab1 = copy.deepcopy(window)
    tab1.run_command("git clone git@github.com:python/cpython.git")
    tab2 = copy.copy(tab1)
    tab2.run_command("cd python/")
    window.run_command("ls -l")
    tab1.run_command("git checkout 3.13")
    pp(vars(window))
    print()
    pp(vars(tab1))
    print()
    pp(vars(tab2))
