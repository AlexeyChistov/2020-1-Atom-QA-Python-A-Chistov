import json
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import urllib.parse

import config
from simple_data_client.data_client import UserClient


class MockHandlerRequest(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def _get_request_data(self):
        content_length = int(self.headers['Content-Length'])
        return self.rfile.read(content_length).decode()

    def do_GET(self):
        user_client = UserClient()
        if self.path == '/':
            data = user_client.show_data()
            self._set_headers(status_code=200)
            self.wfile.write(data.encode())
        elif self.path == '/timeout':
            time.sleep(2)
            self._set_headers(status_code=200)
        elif self.path == '/500':
            self._set_headers(status_code=500)
        else:
            self._set_headers(status_code=404)

    def do_POST(self):
        if self.path == '/reg':
            data = urllib.parse.parse_qs(self._get_request_data())
            username_header = self.headers.get('username')
            if not username_header or username_header != data["username"][0]:
                self._set_headers(status_code=412)
                return
            user_client = UserClient()
            if data["username"][0] == username_header:
                user_client_response = user_client.registration(username_header)
                if user_client_response == "User added":
                    self._set_headers(status_code=201)
                else:
                    self._set_headers(status_code=204)
        else:
            self._set_headers(status_code=404)

    def do_PUT(self):
        if self.path == '/':
            username_header = self.headers.get('username')
            post_title_header = self.headers.get('post_title')
            data = urllib.parse.parse_qs(self._get_request_data())
            if not username_header or not post_title_header:
                self._set_headers(status_code=412)
                return
            if data["username"][0] != username_header or data["post_title"][0] != post_title_header:
                self._set_headers(status_code=412)
                return
            user_client = UserClient()
            if data["username"][0] == username_header and data["post_title"][0] == post_title_header:
                user_client_response = user_client.idempotent_create_post(username_header, post_title_header)
                if user_client_response == "New post created":
                    self._set_headers(status_code=201)
                elif user_client_response == "Post already exists":
                    self._set_headers(status_code=204)
                elif user_client_response == "User doesnt exists":
                    self._set_headers(status_code=404)
        else:
            self._set_headers(status_code=404)


class MockHTTPServer:
    def __init__(self, host, port):
        self.server_run = None
        self.host = host
        self.port = port
        self.handler = MockHandlerRequest
        self.server = HTTPServer((self.host, self.port), self.handler)

    def start(self):
        self.server.allow_reuse_address = True
        th = threading.Thread(target=self.server.serve_forever, daemon=True)
        th.start()
        th.join(1)
        self.server_run = True
        return self.server

    def stop(self):
        self.server.server_close()
        self.server.shutdown()
        self.server_run = False
