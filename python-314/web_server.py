import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

HOSTNAME = "localhost"
PORT = 8000


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        user_agent = self.headers.get("User-Agent")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"Hello, {user_agent}".encode())


def main():
    print(f"Starting the server on: http://{HOSTNAME}:{PORT}")
    print("Run this command as a superuser to attach the debugger:")
    print(f"{sys.executable} -m pdb -p {os.getpid()}")
    HTTPServer((HOSTNAME, PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
