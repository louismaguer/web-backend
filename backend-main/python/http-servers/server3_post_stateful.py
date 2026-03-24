"""
This server is stateful, it keeps the data in a global variable STATE.
- one can record var=value using a POST request to /api/register
- a GET (on any path) will display the current state as HTML
"""

# pylint: disable = missing-docstring, invalid-name

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

STATE = {}

class EchoHttpHandlerWithPOST(BaseHTTPRequestHandler):

    def do_GET(self):
        client_addr = self.client_address
        request_path = self.path

        self.send_response(200)
        self.send_header(b'Content-type', b'text/html')
        self.end_headers()
        self.wfile.write(f"""
                         <h1>GET request</h1>
                         <ul>
                             <li>client={client_addr}</li>
                             <li>path={request_path}</li>
                             <li>data_saved={STATE}</li>
                        </ul>
                        """.encode())


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

PORT = 9002
print(f"Open this in your browser:\nhttp://localhost:{PORT}/index.html")

server = HTTPServer(("", PORT), EchoHttpHandlerWithPOST)
server.serve_forever()
