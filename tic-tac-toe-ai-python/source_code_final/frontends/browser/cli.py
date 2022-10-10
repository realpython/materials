import http.server
import socketserver
import threading
import webbrowser

PORT = 8000


def run_server(port: int = PORT) -> None:
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving HTTP on http://127.0.0.1:{port}/ ...")
        httpd.serve_forever()


def open_browser(port: int = PORT) -> None:
    webbrowser.open(f"http://127.0.0.1:{port}/browser/index.html")


def main() -> None:
    threading.Thread(target=open_browser).start()
    run_server()
