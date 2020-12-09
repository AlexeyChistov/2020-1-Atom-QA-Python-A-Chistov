import pytest
from _pytest.fixtures import FixtureRequest

from API.api_client import ApiClient
from test_data import users
from test_data.data_generator import DataGenerator


class BaseCaseApi:
    """
    Наш автоюз для API:
    """
    SUPER_USER = users.SUPER_USER_KEYS[0]
    SUPER_USER_PASSWORD = users.SUPER_USER[f"{SUPER_USER}"][0]
    SUPER_USER_PASSWORD_EMAIL = users.SUPER_USER[f"{SUPER_USER}"][1]
    SIMPLE_USER = users.SIMPLE_USER
    SIMPLE_PASSWORD = users.SIMPLE_PASSWORD
    SIMPLE_EMAIL = users.SIMPLE_EMAIL

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, request: FixtureRequest):
        if "API" in request.keywords:
            self.api_page: ApiClient = request.getfixturevalue('api_page')
            return
        if "API_401" in request.keywords:
            self.api_page_401: ApiClient = request.getfixturevalue('api_page_401')
            return

    @pytest.fixture(scope='function')
    def generator(self, request: FixtureRequest):
        self.generator: DataGenerator = request.getfixturevalue('generator')

    @pytest.fixture(scope='function')
    def auto_api_registration(self, request: FixtureRequest):
        """
        Фикстурка для добавления "простого" пользователя
        Возвращает username пользователя
        """
        username = self.SIMPLE_USER
        password = self.SIMPLE_PASSWORD
        email = self.SIMPLE_EMAIL
        api_page: ApiClient = request.getfixturevalue('api_page')
        api_page.add_user(username, password, email)
        return username
