"""
kind of cheating as it leverages the standard library
but this is the simplest static server
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler

handler = SimpleHTTPRequestHandler

PORT = 9000
print(f"Open this in your browser:\nhttp://localhost:{PORT}/index.html")

httpd = HTTPServer(('', PORT),  handler)
httpd.serve_forever()
