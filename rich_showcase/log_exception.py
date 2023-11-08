import time
from rich.traceback import install
from rich.console import Console
from rich.theme import Theme
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})
install(show_locals=True)
console = Console(theme=custom_theme)

console.log("Nothing happening here", style="info")
console.log("Trouble brewing...", style="warning")
time.sleep(1)
console.log("Bad news!!", style="danger")
raise RuntimeError("Things haven't worked out as we hoped")
