import json

import pytest

from fixtures.base_case_api import BaseCaseApi


class TestAccept(BaseCaseApi):

    @pytest.mark.API
    def test_accept_1(self, auto_api_registration):
        """
        Позитив тест на разблокировку
        Проверяем статус код и фактическое изменение в таблице
        """
        username = auto_api_registration
        self.api_page.block_user(username)
        response = self.api_page.accept_user(username)
        response_from_table = self.api_page.check_user(username)
        self.api_page.delete_user(username)
        assert response.status_code == 200
        assert json.loads(response_from_table.text)["access"] == 1

    @pytest.mark.API
    def test_accept_2(self, auto_api_registration):
        """
        Проверка фактического изменениея в таблице
        """
        username = auto_api_registration
        self.api_page.block_user(username)
        response = self.api_page.accept_user(username)
        response_from_table = self.api_page.check_user(username)
        self.api_page.delete_user(username)
        assert response.status_code == 200
        assert json.loads(response_from_table.text)["access"] == 1
