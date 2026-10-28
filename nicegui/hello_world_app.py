from nicegui import app, ui

app.native.window_args["resizable"] = False

ui.page_title("Hello World!")
ui.label("Hello World!")

ui.run(native=True, window_size=(800, 700))