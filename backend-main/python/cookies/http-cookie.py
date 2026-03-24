"""
this app sets a cookie in the browser called 'visit'
that tracks the number of times the user has visited the page.

using only the Python standard library
this gives a rather long/tedious version
but it's interesting to compare it with the fastapi version

NOTES:
- of course you don't want to write this kind of low-lever code in real life
- when running this, you'll see the counter increase TWICE per page load
  this is because the browser requests /favicon.ico automatically
  and since we don't handle that path, it gets counted as well
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
from random import randint


class SessionHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        routes = {
            "/": self.home,
            "/index.html": self.home,
        }
        self.cookie = None
        print(self.path)
        # try:
        response = 200
        cookies = self.parse_cookies(self.headers["Cookie"])
        if "visit" in cookies:
            self.visit = int(cookies["visit"]) + 1
        else:
            self.visit = 0

        try:
            self.cookie = f"visit={self.visit}"
            # call the callback attached to the endpoint
            content = routes[self.path]()
        except Exception as e:
            response = 404
            content = "Not Found"

        self.send_response(response)
        self.send_header("Content-type", "text/html")

        if self.cookie:
            print(self.cookie)
            self.send_header("Set-Cookie", self.cookie)

        self.end_headers()
        self.wfile.write(content.encode("utf-8"))
        return

    def home(self):
        return (
            "<h1>Welcome for your first time here !</h1>"
            if self.visit == 0
            else
            f"<h1>You have seen this page {self.visit} times !</h1>"
        )

    def parse_cookies(self, cookie_list):
        ret = {}
        if not cookie_list:
            return ret
        for c in cookie_list.split(";"):
            tokens = c.split("=")
            ret[tokens[0].strip()] = "".join(tokens[1:])
        return ret

PORT = 10000
print(f"Open this in your browser:\nhttp://localhost:{PORT}/")

address = ("", PORT)
handler = SessionHandler
server = HTTPServer(address, handler)
server.serve_forever()
