from fixtures.base import BaseCase
from ui.user.data import UserData
import pytest


class TestLogin(BaseCase):
    @pytest.mark.UI
    def test_login_success(self):
        """Тест на успешную авторизацию"""
        assert self.login_page.login_success(UserData.USER_MAIL, UserData.USER_PASS)

    @pytest.mark.UI
    def test_login_failed(self):
        """Тест на провальную авторизацию"""
        assert self.login_page.login_failed('wrong@mail.ru', 'wrongpassword')
