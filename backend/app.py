#!/usr/bin/env python3
"""Simple HTTP server responding with "Hello from DevOps Example!" on root path."""

import http.server
import socketserver

PORT = 8080


class HelloHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = b"Hello from DevOps Example!"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        else:
            self.send_error(404, "Not Found")


if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), HelloHandler) as httpd:
        print(f"Server listening on port {PORT}")
        httpd.serve_forever()
