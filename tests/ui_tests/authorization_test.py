import json

import pytest
from selenium.webdriver.common.by import By

from fixtures.base_case_ui import BaseCaseUi
from test_data import users


class TestAuthorization(BaseCaseUi):
    SUPER_USER = users.SUPER_USER_KEYS[0]
    SUPER_USER_PASSWORD = users.SUPER_USER[f"{SUPER_USER}"][0]

    @pytest.mark.UI
    def test_login_1(self):
        """Первый шаблон авторизации:"""
        self.base_page.login_1(self.SUPER_USER, self.SUPER_USER_PASSWORD)
        assert "Test Server" in self.base_page.driver.title

    @pytest.mark.UI
    def test_login_2(self):
        """Второй шаблон авторизации:"""
        self.base_page.login_2(self.SUPER_USER, self.SUPER_USER_PASSWORD)
        assert "Test Server" in self.base_page.driver.title

    @pytest.mark.UI
    def test_login_3(self):
        """Третий шаблон авторизации:"""
        self.base_page.login_3(self.SUPER_USER, self.SUPER_USER_PASSWORD)
        assert "Test Server" in self.base_page.driver.title

    @pytest.mark.UI
    def test_check_id(self, init_api):
        """Проверяем, что id пользователя отображается корректно:"""
        self.base_page.login_3(self.SUPER_USER, self.SUPER_USER_PASSWORD)
        response_from_table = (self.api_page.check_user(self.SUPER_USER))
        user_data = json.loads(response_from_table.text)
        user_id = user_data["id"]
        assert self.base_page.find(self.main_page.main_page_locators.VK_ID) == \
               self.base_page.find((By.XPATH, f'//li[contains(text(), "VK ID: {user_id}")]'))

    @pytest.mark.skip(reason="no need")
    @pytest.mark.UI
    def test_check_username(self):
        """Проверяем, что имя пользователя отображается корректно:"""
        self.base_page.login_3(self.SUPER_USER, self.SUPER_USER_PASSWORD)
        assert self.base_page.find(self.main_page.main_page_locators.LOGGED_AS) == \
               self.base_page.find((By.XPATH, f'//li[contains(text(), "Logged as {self.SUPER_USER}")]'))
