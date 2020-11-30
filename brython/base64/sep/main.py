from browser import document, prompt, html  # type: ignore
import base64

b64_map = {}


def base64_compute(_) -> None:
    default = "Real Python"
    data = prompt("Enter a string:", default)
    data = data or default
    b64data = base64.b64encode(data.encode()).decode()
    b64_map[data] = b64data
    display_map()


def display_map() -> None:
    table = html.TABLE(style={"border": "1 solid grey"})
    table <= html.TR(html.TH("Text") + html.TH("Base64"))
    table <= (html.TR(html.TD(key) + html.TD(b64_map[key])) for key in b64_map)
    base64_display = document["b64-display"]
    base64_display.clear()
    base64_display <= table


document["b64-btn"].bind("click", base64_compute)
