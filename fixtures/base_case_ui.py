import pytest
from _pytest.fixtures import FixtureRequest

from API.api_client import ApiClient
from UI.pages.base_page import BasePage
from UI.pages.main_page import MainPage
from UI.pages.registration_page import RegistrationPage
from test_data import users


class BaseCaseUi:
    """
    Наш автоюз для UI:
    прокидываем в UI marked тесты драйвер, конфиг, ui_pages;
    """
    SUPER_USER = users.SUPER_USER_KEYS[0]
    SUPER_USER_PASSWORD = users.SUPER_USER[f"{SUPER_USER}"][0]
    SUPER_USER_PASSWORD_EMAIL = users.SUPER_USER[f"{SUPER_USER}"][1]
    SIMPLE_USER = users.SIMPLE_USER
    SIMPLE_PASSWORD = users.SIMPLE_PASSWORD
    SIMPLE_EMAIL = users.SIMPLE_EMAIL

    @pytest.fixture(scope='function', autouse=True)
    # def setup(self, driver, config, request: FixtureRequest):
    def setup(self, driver, request: FixtureRequest):
        if "UI" in request.keywords:
            self.driver = driver
            # self.config = config
            self.base_page: BasePage = request.getfixturevalue('base_page')
            self.registration_page: RegistrationPage = request.getfixturevalue('registration_page')
            self.main_page: MainPage = request.getfixturevalue('main_page')
            return

    @pytest.fixture(scope='function')
    def init_api(self, request: FixtureRequest):
        """
        При необходимости пробрасываем api клиента
        """
        self.api_page: ApiClient = request.getfixturevalue('api_page')
