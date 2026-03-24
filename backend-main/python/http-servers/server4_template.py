"""
same functions as server3
but this time we use a template to render the html
which makes it easier to maintain (separation of concerns)
"""

# pylint: disable = missing-docstring, invalid-name

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from jinja2 import Template

STATE = {}

class EchoHttpHandlerWithPOST(BaseHTTPRequestHandler):

    def do_GET(self):
        client_addr = self.client_address
        request_path = self.path

        self.send_response(200)
        self.send_header(b'Content-type', b'text/html')
        self.end_headers()
        # -------
        # this is the part that changes from previous example
        # Assuming we start the server from the repo root
        with open("python/http-servers/template.html.j2", "r") as f:
            template = f.read()
            # the variable names we can use in the template
            env = dict(
                client=client_addr,
                path=request_path,
                data=STATE,
            )
            html = Template(template).render(env)
            self.wfile.write(html.encode())
        # -------


    def do_POST(self):
        client_addr = self.client_address
        print(f"Server received POST from {client_addr} for path {self.path}")
        request_path = self.path
        if request_path == "/api/register":
            # Read the data
            data_size = int(self.headers["Content-Length"])
            self.log_message( f"data_size = {data_size}")
            data_raw = self.rfile.read(data_size).decode()
            data_json = json.loads(data_raw)
            # expect a dicionary
            if not isinstance(data_json, dict):
                self.send_response(400)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Expected a dictionary")
                return
            for k, v in data_json.items():
                STATE[k] = v
            print(f"Server received data: {data_json}")
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(STATE).encode())
        else:
            self.send_response(404)

PORT = 9003
print(f"Open this in your browser:\nhttp://localhost:{PORT}/index.html")

server = HTTPServer(("", PORT), EchoHttpHandlerWithPOST)
server.serve_forever()
