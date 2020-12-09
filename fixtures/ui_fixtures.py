import pytest
from _pytest.fixtures import FixtureRequest

from UI.pages.base_page import BasePage
from test_data import users


@pytest.fixture(scope='function')
def auto_auth(request: FixtureRequest):
    """
    Для всех тестов, кроме тестов на авторизацию/регистрацию
    """
    base_page: BasePage = request.getfixturevalue('base_page')
    test_user = users.SUPER_USER_KEYS[0]
    password = users.SUPER_USER[f"{test_user}"][0]
    base_page.login_1(test_user, password)
