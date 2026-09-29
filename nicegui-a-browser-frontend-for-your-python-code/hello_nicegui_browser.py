from nicegui import ui

ui.label("Hello, NiceGUI!")
ui.button("Click me", on_click=lambda: ui.notify("It works!"))
ui.run()
