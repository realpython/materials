from browser import document, prompt


def hello(evt):
    default = "Real Python"
    name = prompt("Enter your name:", default)
    if not name:
        name = default
    document["hello"].innerHTML = f"Hello, {name}!"


document["hello-btn"].bind("click", hello)
