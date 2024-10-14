import re
from textual.app import App
from textual.widgets import Button, Static, Input
from textual.containers import Container
from textual.reactive import reactive

class BinaryCalculatorApp(App):
    CSS_PATH = "binary_calculator.tcss"
    # Initializing the reactive state variables
    result = reactive("0")
    expression = reactive("")

    def compose(self):
        """Create child widgets for the app."""
        yield Static("Binary Calculator", id="header")
        yield Input(placeholder="Enter binary numbers...", id="input")
        yield Static(id="result", name="Result")
        with Container( id="buttons"):
            yield Button(label="0", id="btn-0")
            yield Button(label="1", id="btn-1")
            yield Button(label="+", id="btn-plus")
            yield Button(label="-", id="btn-minus")
            yield Button(label="*", id="btn-mul")
            yield Button(label="/", id="btn-div")
            yield Button(label="C", id="btn-clear")
            yield Button(label="=", id="btn-equals") 

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        btn = event.button.id

        if btn == "btn-clear":
            self.expression = ""
            self.result = "0"
        elif btn == "btn-equals":
            try:
                # Evaluating the binary expression
                expr = self.convert_expression()
                expr = re.sub('([01]+)','0b\\1',expr)
                res = bin(eval(expr))
                # Remove the "0b" prefix for display purposes
                if res.startswith('-'):
                    self.result = '-' + str(res)[3:]
                else:
                    self.result = str(res)[2:]
            except Exception:
                self.result = "Error"
        else:
            # Update the expression based on button press
            if btn.startswith("btn-"):
                value = btn.split("-")[-1]
                self.expression += value
                self.expression = self.convert_expression()

    def convert_expression(self):
        """Convert the binary expression to a format that Python can evaluate."""
        exp = self.expression.replace("plus", " + ").replace("minus", " - ").replace("mul", " * ").replace("div", " // ")
        return exp

    def watch_result(self, result: str) -> None:
        """Update the result display."""
        self.query_one("#result").update(f"Result: {result}")

    def watch_expression(self, expression: str) -> None:
        """Update the input display with the current expression."""
        self.query_one(Input).value = expression

# Running the app
if __name__ == "__main__":
    app = BinaryCalculatorApp()
    app.run()
