import json

import pytest

from fixtures.base_case_api import BaseCaseApi


class TestBlock(BaseCaseApi):

    @pytest.mark.API
    def test_block_pos_1(self):
        """
        Позитив тест на блокировку
        Ожидаем 200 от приложения и сообщения "User was blocked!
        """
        self.api_page.add_user("Alexey", "123", "aa.@aa.aa")
        response = self.api_page.block_user("Alexey")
        self.api_page.delete_user("Alexey")
        assert response.status_code == 200
        assert response.text == "User was blocked!"

    @pytest.mark.API
    def test_block_pos_2(self):
        """
        Позитив тест на блокировку пользователя
        Проверяем фактическое изменение в таблице значения "access"
        """
        self.api_page.add_user("Alexey", "123", "aa.@aa.aa")
        self.api_page.block_user("Alexey")
        response_from_table = (self.api_page.check_user("Alexey"))
        self.api_page.delete_user("Alexey")
        assert json.loads(response_from_table.text)["access"] == 0

    @pytest.mark.API_401
    def test_block_neg_1(self):
        """
        Негатив тест на блокировку
        Авторизация не произведена
        Ожидаем 401 от приложения
        """
        response = self.api_page_401.block_user("Alexey")
        assert response.status_code == 401

    @pytest.mark.API
    def test_block_neg_2(self):
        """
        Негатив тест на блокировку
        Пытаемся заблокировать пользователя, которого нет в таблице
        Ожидаем 404 от приложения
        """
        response = self.api_page.block_user("Alexey")
        assert response.status_code == 404
