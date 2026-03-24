"""
same functions: as server1: serves static files
but this time we do the coding by hand
"""

# pylint: disable = attribute-defined-outside-init, unspecified-encoding, missing-docstring, invalid-name

from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        client_addr = self.client_address
        print(f"Server received req from {client_addr} for path {self.path}")
        if self.path == "/":
            print("Hiya, asking for root, let's respond with index.html")
            self.path = "index.html"
        try:
            localfile = Path(f"./{self.path}")
            with localfile.open('rb') as f:
                content = f.read()
            self.send_response(200)
            match localfile.suffix:
                case '.html':
                    self.send_header('Content-type', 'text/html')
                case '.js':
                    self.send_header('Content-type', 'application/javascript')
                case '.css':
                    self.send_header('Content-type', 'text/css')
                case _:
                    self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(content)
        except IOError as exc:
            print(exc)
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<h1>404: File not found</h1>')

PORT = 9001
print(f"Open this in your browser:\nhttp://localhost:{PORT}/index.html")

httpd = HTTPServer(('', PORT),  MyHandler)
httpd.serve_forever()
