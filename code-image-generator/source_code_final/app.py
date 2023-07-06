import base64

from flask import Flask, render_template, request, session, url_for
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import Python3Lexer
from pygments.styles import get_all_styles

from utils import make_screenshot

app = Flask(__name__)
app.secret_key = "mysecretkey"


DEFAULT_CODE = "print('Hello, World!')"
DEFAULT_THEME = "default"


@app.route("/", methods=["POST", "GET"])
def code():
    if request.method == "POST" and "reset" in request.form.keys():
        session["code"] = DEFAULT_CODE
    code = session.get("code") or DEFAULT_CODE
    lines = code.split("\n")
    context = {
        "message": "Add Python Code 🐍",
        "code": code,
        "num_lines": len(lines),
        "max_chars": len(max(lines, key=len)),
    }
    app.logger.info(context)
    return render_template("code_input.html", **context)


@app.route("/theme", methods=["POST", "GET"])
def theme():
    if request.method == "POST":
        session["code"] = request.form.get("code") or session.get("code")
        session["theme"] = request.form.get("theme") or session.get("theme")
    theme = session.get("theme") or DEFAULT_THEME
    formatter = HtmlFormatter(style=theme)
    context = {
        "message": "Select Your Theme 🎨",
        "code": session["code"],
        "all_themes": list(get_all_styles()),
        "theme": theme,
        "theme_bg_color": formatter.style.background_color,
        "style": formatter.get_style_defs(),
        "code_highlighted": highlight(
            session["code"], Python3Lexer(), formatter
        ),
    }
    return render_template("theme_selection.html", **context)


@app.route("/preview", methods=["POST", "GET"])
def preview():
    if request.method == "POST":
        session["theme"] = request.form.get("theme") or session.get("theme")
    theme = session.get("theme")
    formatter = HtmlFormatter(style=theme)
    context = {
        "message": "Preview Your Picture 🖼️",
        "code": session["code"],
        "all_themes": list(get_all_styles()),
        "theme": theme,
        "theme_bg_color": formatter.style.background_color,
        "style": formatter.get_style_defs(),
        "code_highlighted": highlight(
            session["code"], Python3Lexer(), formatter
        ),
    }
    return render_template("preview.html", **context)


@app.route("/screenshot", methods=["POST", "GET"])
def screenshot():
    context = {"message": "No screenshot yet 👀"}
    if request.method == "POST":
        session["theme"] = request.form.get("theme") or session.get("theme")
        session_dict = {
            "name": app.config["SESSION_COOKIE_NAME"],
            "value": request.cookies.get(app.config["SESSION_COOKIE_NAME"]),
            "url": request.host_url,
        }
        target_url = request.host_url + url_for("theme")
        screenshot_bytes = make_screenshot(target_url, session_dict)
        context["message"] = "Done! 🎉"
        context["screenshot_b64"] = base64.b64encode(screenshot_bytes).decode()
    return render_template("screenshot.html", **context)
    return render_template("screenshot.html", **context)
