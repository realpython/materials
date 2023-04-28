import json
import mimetypes
import webbrowser
from functools import cached_property
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qsl, urlparse


class WebRequestHandler(BaseHTTPRequestHandler):
    @cached_property
    def url(self):
        return urlparse(self.path)

    @cached_property
    def query_data(self):
        return dict(parse_qsl(self.url.query))

    @cached_property
    def post_data(self):
        content_length = int(self.headers["Content-Length"])
        return self.rfile.read(content_length)

    @cached_property
    def form_data(self):
        return dict(parse_qsl(self.post_data.decode("utf-8")))

    @cached_property
    def cookies(self):
        return SimpleCookie(self.headers.get("Cookie"))

    def do_GET(self):
        self.send_error(404)

    def do_POST(self):
        self.send_error(404)


class StaticView(WebRequestHandler):
    STATIC_DIR = Path("static")
    STATIC_PATH = "/static"

    def do_GET(self):
        if self.url.path.startswith(self.STATIC_PATH):
            self.send_file(self.STATIC_DIR / Path(self.url.path).name)
        else:
            super().do_GET()

    def send_file(self, path, encoding="utf-8"):
        if path.exists() and path.is_file():
            mime_type, _ = mimetypes.guess_type(path)
            if mime_type.startswith("text/"):
                content_type = f"{mime_type}; charset={encoding}"
            else:
                content_type = mime_type
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.end_headers()
            self.wfile.write(path.read_bytes())
        else:
            self.send_error(404)


class DynamicView(WebRequestHandler):
    TEMPLATES_DIR = Path("templates")

    def send_redirect(self, location, extra_headers=None):
        self.send_response(302)
        self.send_header("Location", location)
        if extra_headers:
            for name, value in extra_headers.items():
                self.send_header(name, value)
        self.end_headers()

    def render_template(self, name, encoding="utf-8", **context):
        self.send_response(200)
        self.send_header("Content-Type", f"text/html; charset={encoding}")
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.end_headers()
        template = (self.TEMPLATES_DIR / name).read_text(encoding)
        self.wfile.write(template.format(**context).encode(encoding))


class MyAppView(StaticView, DynamicView):
    SESSION_COOKIE = "session"
    USERS_DATABASE = Path("users.json")

    def do_GET(self):
        match self.url.path:
            case "/":
                self.home_view()
            case "/login":
                self.login_view()
            case "/logout":
                self.logout_view()
            case _:
                super().do_GET()

    def do_POST(self):
        if self.url.path == "/login":
            self.handle_login_form()
        else:
            super().do_POST()

    @property
    def users(self):
        with self.USERS_DATABASE.open(encoding="utf-8") as file:
            return json.load(file)

    @property
    def logged_in(self):
        return self.SESSION_COOKIE in self.cookies

    @property
    def logged_user(self):
        return self.cookies[self.SESSION_COOKIE].value

    def home_view(self):
        if self.logged_in:
            self.render_template("home_view.html", username=self.logged_user)
        else:
            self.send_redirect("/login")

    def login_view(self):
        if self.logged_in:
            self.send_redirect("/")
        else:
            hidden = "" if "failed" in self.query_data else "hidden"
            self.render_template("login_form.html", hidden=hidden)

    def logout_view(self):
        self.send_redirect(
            "/login",
            extra_headers={"Set-Cookie": f"{self.SESSION_COOKIE}=; Max-Age=0"},
        )

    def handle_login_form(self):
        try:
            username = self.form_data["username"]
            password = self.form_data["password"]
        except KeyError:
            self.send_error(400)
        else:
            if self.authenticate(username, password):
                self.send_redirect(
                    "/",
                    extra_headers={
                        "Set-Cookie": f"{self.SESSION_COOKIE}={username}"
                    },
                )
            else:
                self.send_redirect("/login?failed=true")

    def authenticate(self, username, password):
        return password == self.users.get(username)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), MyAppView)
    webbrowser.open("http://{0}:{1}".format(*server.server_address))
    server.serve_forever()
