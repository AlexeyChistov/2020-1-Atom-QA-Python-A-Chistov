import pytest
from time import sleep
from _pytest.fixtures import FixtureRequest
from config import Config
from app.flask_app import FlaskApp
from mock.http_mock import MockHTTPServer
from simple_data_client.data_client import UserClient
from sokcet_client.socket_client import SocketRequests


class Base:
    @pytest.fixture(scope='session', autouse=True)
    def run_app_and_mock(self, request: FixtureRequest):
        self._flask_app: FlaskApp = request.getfixturevalue('flask_app')
        self._http_mock: MockHTTPServer = request.getfixturevalue('http_mock')
        self._app_socket_requests: SocketRequests = request.getfixturevalue('app_socket_requests')
        app_server = self._flask_app.run_app()
        mock_server = self._http_mock.start()
        yield app_server, mock_server
        self._http_mock.stop()
        self._app_socket_requests.get('/shutdown')

    @pytest.fixture(scope='function', autouse=True)
    def init_socket_requests(self, request: FixtureRequest):
        self.app_socket_requests: SocketRequests = request.getfixturevalue('app_socket_requests')
        sleep(2)
        self.mock_socket_requests: SocketRequests = request.getfixturevalue('mock_socket_requests')
        sleep(2)
        self.user_client: UserClient = UserClient()
        return self.app_socket_requests, mock_socket_requests, self.user_client


@pytest.fixture()
def init_http_mock(request: FixtureRequest):
    http_mock: MockHTTPServer = request.getfixturevalue('http_mock')
    return http_mock


@pytest.fixture(scope='session')
def flask_app():
    return FlaskApp(Config.APP_HOST, Config.APP_PORT)


@pytest.fixture(scope='session')
def http_mock():
    return MockHTTPServer(Config.MOCK_HOST, Config.MOCK_PORT)


@pytest.fixture(scope='session')
def app_socket_requests():
    return SocketRequests(Config.APP_HOST, Config.APP_PORT)


@pytest.fixture(scope='session')
def mock_socket_requests():
    return SocketRequests(Config.MOCK_HOST, Config.MOCK_PORT)
