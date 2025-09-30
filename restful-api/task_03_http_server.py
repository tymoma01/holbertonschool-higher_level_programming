"""
Simple HTTP API using Python's http.server

Expected behavior:
- GET /           -> "Hello, this is a simple API!"
- GET /data       -> {"name": "John", "age": 30, "city": "New York"}
- GET /info       -> {"version": "1.0", "description": "A simple API built with http.server"}
- Any other path  -> 404 Not Found with "Endpoint not found"
"""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    # --- Utility helpers -----------------------------------------------------

    def _send_text(self, status: int, text: str, content_type: str = "text/plain; charset=utf-8"):
        body = text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, status: int, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # --- HTTP methods --------------------------------------------------------

    def do_GET(self):
        path = urlparse(self.path).path

        if path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif path == "/data":
            payload = {"name": "John", "age": 30, "city": "New York"}
            self._send_json(200, payload)
        elif path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self._send_json(200, info)
        else:
            self._send_text(404, "Endpoint not found")

    # Explicitly return 405 for unsupported methods (optional but nice)
    def do_POST(self):
        self._send_text(405, "Method Not Allowed")

    def do_PUT(self):
        self._send_text(405, "Method Not Allowed")

    def do_DELETE(self):
        self._send_text(405, "Method Not Allowed")

    # Reduce default logging noise if desired
    def log_message(self, format, *args):
        return 


def run(host: str = "localhost", port: int = 8000):
    server = ThreadingHTTPServer((host, port), SimpleAPIHandler)
    print(f"Server running on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        print("\nServer stopped.")


if __name__ == "__main__":
    run()
