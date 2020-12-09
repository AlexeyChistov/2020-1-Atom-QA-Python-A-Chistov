import json

import pytest

from fixtures.base_case_api import BaseCaseApi


class TestAdd(BaseCaseApi):

    # @pytest.mark.skip(reason="no need")
    @pytest.mark.API
    def test_add_positive_1(self, generator):
        """
        Позитив тест на добавление, отылаем валидные данные
        Ожидаем 201 от приложения
        """
        username = self.generator.generate_valid_username_field()
        password = self.generator.generate_valid_password_field()
        email = self.generator.generate_valid_email_field(random=False)
        response = self.api_page.add_user(username, password, email)
        self.api_page.delete_user(username)
        assert response.status_code == 201
        assert response.text == "User was added!"

    # @pytest.mark.skip(reason="no need")
    @pytest.mark.API
    def test_add_positive_2(self, generator, auto_api_registration):
        """
        Позитив тест на добавление пользователя
        Проверяем значения в самой таблице, при добавлении пользователя
        Ожидаем, что в полее access проставится 1
        """
        username = auto_api_registration
        response_from_table = self.api_page.check_user(username)
        self.api_page.delete_user(username)
        assert json.loads(response_from_table.text)["access"] == 1

    # @pytest.mark.skip(reason="no need")
    @pytest.mark.API
    def test_add_positive_3(self, generator, auto_api_registration):
        """
        Позитив тест на добавление
        Проверяем значения в самой таблице, при добавлении пользователя
        Ожидаем, что в поле active проставится 1
        """
        username = auto_api_registration
        response_from_table = self.api_page.check_user(username)
        self.api_page.delete_user(username)
        assert json.loads(response_from_table.text)["active"] == 1


    # @pytest.mark.skip(reason="no need")
    @pytest.mark.API
    def test_add_positive_4(self):
        """
        Позитив тест на добавление
        Пытаемся добавить пользователя второй раз, ожидаем 304
        """
        username = self.SIMPLE_USER
        password = self.SIMPLE_PASSWORD
        email = self.SIMPLE_EMAIL
        self.api_page.add_user(username, password, email)
        response = self.api_page.add_user(username, password, email)
        self.api_page.delete_user(username)
        assert response.status_code == 304
        assert response.text == ""

    # @pytest.mark.skip(reason="no need")
    @pytest.mark.API_401
    def test_add_user_neg_1(self):
        """
        Негатив тест на блокировку
        Проверяем статус код ответа
        Проверяем фактическое изменение в таблице значения "access"
        """
        username = self.SIMPLE_USER
        response = self.api_page_401.block_user(username)
        assert response.status_code == 401

    @pytest.mark.API
    def test_add_user_neg_2(self, generator):
        """
        Пытаемя отослать некорректные данные
        """
        username = self.generator.generate_invalid_username_field_overflow()
        password = self.generator.generate_invalid_password_field()
        email = self.generator.generate_invalid_email_field_value()
        response = self.api_page.add_user(username, password, email)
        self.api_page.delete_user(username)
        assert response.status_code == 201
