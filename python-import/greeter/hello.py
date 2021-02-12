# greeter/hello.py
import plugins


@plugins.register
def greet(name):
    print(f"Hello {name}, how are you today?")
