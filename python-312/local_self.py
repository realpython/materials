import inspect


class Greeter:
    def __init__(self):
        self.message = "Hello"

    def greet(self, whom="World"):
        frame = inspect.currentframe()
        wrong_name = "message"

        if "self" in frame.f_locals:
            self = frame.f_locals["self"]
            if hasattr(self, wrong_name):
                raise NameError(
                    (
                        f"name '{wrong_name}' is not defined. "
                        f"Did you mean: 'self.{wrong_name}'?"
                    )
                )


Greeter().greet()
