import random
from string import hexdigits

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def generate_color():
    return f"#{''.join(random.choices(hexdigits.lower(), k=6))}"


@app.get("/", response_class=HTMLResponse)
def home():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Home</title>
    </head>
    <body>
        <h1>Welcome to FastAPI!</h1>
    </body>
    </html>
    """
    return html


@app.get("/random-color", response_class=HTMLResponse)
def random_color(request: Request):
    color = generate_color()
    return templates.TemplateResponse(
        request=request, name="color.html", context={"color": color}
    )
