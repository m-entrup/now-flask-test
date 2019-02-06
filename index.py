"""
This is an example that can be found at https://zeit.co/docs/v2/deployments/official-builders/python-now-python/

Use `pipenv install -r requirements.txt` to install all requirements.
"""

from http.server import BaseHTTPRequestHandler
from cowpy import cow


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = cow.Cowacter().milk('Hello from Python on Now Lambda!1111111')
        self.wfile.write(message.encode())
        return
