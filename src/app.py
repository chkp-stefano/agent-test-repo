"""A tiny status service. Nothing here is real — it exists so the demo has code."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8080


class StatusHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"status": "ok", "version": VERSION}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


VERSION = "0.1.0"


def main():
    # Loopback only; this is a local dev stub.
    HTTPServer(("127.0.0.1", PORT), StatusHandler).serve_forever()


if __name__ == "__main__":
    main()