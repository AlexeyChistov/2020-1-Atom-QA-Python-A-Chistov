import socket
import urllib.parse
from time import sleep
socket.setdefaulttimeout(2)


class SocketRequests:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def _create_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(2)
        self.sock.connect((self.host, self.port))
        self.sock.settimeout(3)

    def _close_socket(self):
        self.sock.close()

    def _send_request(self, request):
        self._create_socket()
        b_request = request.encode()
        self.sock.send(b_request)
        response = self._get_response()
        self._close_socket()
        sleep(1)
        return response

    def _get_response(self):
        all_data = []
        while True:
            data = self.sock.recv(8192)
            if data:
                all_data.append(data.decode())
            else:
                break
        data = ''.join(all_data).splitlines()
        return data[-1]

    def get(self, endpoint):
        request = f'Get {endpoint} HTTP/1.1\r\n' \
                  f'Host:{self.host}:{self.port}\r\n\r\n'
        response = self._send_request(request)
        return response

    def put(self, endpoint, data, header=None):
        if header is None:
            header = {}
        encoded_data = urllib.parse.urlencode(data)
        request_header = ""
        if header != {}:
            for key in header.keys():
                request_header += key + ": " + header[key] + '\r\n'
        content_len = len(encoded_data)
        request = f'Put /{endpoint}/{data["username"]}/{data["post_title"]} HTTP/1.1\r\n' \
                  f'Host:{self.host}:{self.port}\r\n' \
                  f'Content-Type: multipart/form-data\r\n' \
                  f'Content-Length: {content_len}\r\n' \
                  f'{request_header}\r\n\r\n'
        response = self._send_request(request)
        return response

    def post(self, endpoint, data, header=None):
        encoded_data = urllib.parse.urlencode(data)
        request_header = ""
        if header is None:
            header = {}
        if header != {}:
            for key in header.keys():
                request_header += key + ": " + header[key] + '\r\n'
        content_len = len(encoded_data)
        request = f'Post /{endpoint}/{data["username"]} HTTP/1.1\r\n' \
                  f'Host:{self.host}:{self.port}\r\n' \
                  f'Content-Length: {content_len}\r\n' \
                  f'{request_header}\r\n\r\n'
        response = self._send_request(request)
        return response
