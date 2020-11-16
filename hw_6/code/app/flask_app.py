import threading
from urllib.parse import urljoin
from flask import request, Flask, jsonify
from config import Config
import requests


class FlaskApp(Config):
    app = Flask(__name__)

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run_app(self):
        server = threading.Thread(target=self.app.run, kwargs={
            "host": self.host,
            "port": self.port
        })
        server.start()
        server.join(1)

        return server

    @staticmethod
    @app.errorhandler(404)
    def err(e):
        return jsonify({"Error": "bad request"}), 404

    @staticmethod
    @app.route('/', methods=['GET'])
    def index():
        response = requests.get(Config.MOCK_URL)
        return response.json()

    @staticmethod
    @app.route('/500')
    def return_500():
        response = requests.get(urljoin(Config.MOCK_URL, "/500"))
        return "Error status code 500", response.status_code

    @staticmethod
    @app.route('/timeout')
    def timeout():
        response = requests.get(urljoin(Config.MOCK_URL, "/timeout"), timeout=1)

    @staticmethod
    @app.route('/create/post/<username>/<post_title>', methods=['PUT'])
    def create_post(username, post_title):
        headers = {
            'username': request.headers.get('username'),
            'post_title': request.headers.get('post_title')
        }
        response = requests.put(
            Config.MOCK_URL,
            headers=headers,
            data={"username": username, "post_title": post_title}
        )
        if response.status_code == 201:
            return "New post added", 200
        elif response.status_code == 204:
            return "Post already exists", 200
        elif response.status_code == 412:
            return "Header error", 412
        else:
            return "Bad request", 404

    @staticmethod
    @app.route('/create/user/<username>', methods=['POST'])
    def add_user(username):
        headers = {
            'username': request.headers.get('username')
        }
        response = requests.post(
            urljoin(Config.MOCK_URL, "/reg"),
            headers=headers,
            data={"username": username}
        )
        if response.status_code == 201:
            return "New user added", 200
        elif response.status_code == 204:
            return "User already exist", 200
        elif response.status_code == 412:
            return "Header error", 412
        else:
            return "Error", response.status_code

    @staticmethod
    @app.route('/shutdown')
    def shutdown_server():
        terminate = request.environ.get('werkzeug.server.shutdown')
        if terminate:
            terminate()
            return {"Server status": "down"}, 500
