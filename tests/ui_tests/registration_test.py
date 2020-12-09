import json

import pytest
from fixtures.base_case_ui import BaseCaseUi
from test_data import data_generator, users


class TestRegistration(BaseCaseUi):
    TEST_USER = users.SUPER_USER_KEYS[0]
    TEST_PASSWORD = password = users.SUPER_USER[f"{TEST_USER}"][0]

    @pytest.mark.UI
    def test_active_time_positive(self, init_api):
        """
        После регистрации идет редирект на главную страницу
        Проверяем, проставляется ли время

        """
        username = "user2020"
        email = "user2020@mail.ru"
        password = "2020"
        password_accepting = password
        accept_flag = True
        self.registration_page.user_registration(
            username=username,
            email=email,
            password=password,
            password_accepting=password_accepting,
            accept_flag=accept_flag
        )
        self.base_page.click(self.main_page.main_page_locators.HOME_BUTTON)
        # assert "Test Server" in self.driver.title
        response_from_table = self.api_page.check_user(username)
        start_active_time = json.loads(response_from_table.text)["start_active_time"]
        self.api_page.delete_user(username)
        try:
            assert start_active_time is not None
        except AssertionError:
            raise Exception("start_active_time should be != None, because user was on the main_page")

    @pytest.mark.UI
    def test_user_already_exists_positive(self, init_api):
        """
        Пытаемся зарегистрироваться с уже существующим юзернэймом
        """
        username = self.TEST_USER
        email = "duplicate@mail.ru"
        password = "duplicate"
        password_accepting = password
        accept_flag = True
        self.registration_page.user_registration(
            username=username,
            email=email,
            password=password,
            password_accepting=password_accepting,
            accept_flag=accept_flag
        )
        assert self.base_page.find(self.registration_page.registration_errors_locators.USER_ALREADY_EXISTS)

    @pytest.mark.UI
    def test_user_already_exists_positive(self, init_api):
        """
        Пытаемся зарегистрироваться с уже существующим юзернэймом
        """
        username = "duplicate"
        email = "duplicate@mail.ru"
        password = "duplicate"
        password_accepting = password
        accept_flag = True
        self.registration_page.user_registration(
            username=username,
            email=email,
            password=password,
            password_accepting=password_accepting,
            accept_flag=accept_flag
        )
        assert self.base_page.find(self.registration_page.registration_errors_locators.USER_ALREADY_EXISTS)

    @pytest.mark.UI
    @pytest.mark.parametrize(
        "username, email, password, password_accepting, accept_flag, scheme",
        data_generator.VALIDATION_DATA
    )
    def test_registration(self, username, email, password, password_accepting, accept_flag, scheme):
        """
        Тесты на регистрацию
        scheme = 1: Корректное заполнение всех полей
        scheme = 2: Корректное заполнение всех полей, username - некорректно
        scheme = 3: Корректное заполнение всех полей, password = accepting_password = invalid
        scheme = 4: Корректное заполнение всех полей кроме email
        scheme = 5: Корректное заполнение всех полей, флаг принятия не выставлен
        scheme = 6: Корректное заполнение всех полей кроме, подтверждение пароля не заполнино
        scheme = 7: Флаг выставлен, все поля заполнены некорректно
        """
        self.registration_page.user_registration(
            username=username,
            email=email,
            password=password,
            password_accepting=password_accepting,
            accept_flag=accept_flag
        )
        self.base_page.wait(4)
        if scheme == 1:
            try:
                assert "Test Server" in self.driver.title
            except AssertionError:
                raise Exception("Unexpected, that email should being validated")
        if scheme == 2:
            assert self.base_page.find(self.registration_page.registration_errors_locators.INCORRECT_USERNAME_LENGTH)
        if scheme == 3:
            try:
                assert not (
                    self.base_page.find(self.registration_page.registration_errors_locators.INTERNAL_SERVER_ERROR)
                )
            except AssertionError:
                raise Exception("500, Internal is incorrect")
        if scheme == 4:
            assert (
                self.base_page.find(self.registration_page.registration_errors_locators.INCORRECT_EMAIL_LENGTH) or
                self.base_page.find(self.registration_page.registration_errors_locators.INVALID_EMAIL_ADDRESS)
            )
        if scheme == 5:
            assert "Test Server" not in self.driver.title
        if scheme == 6:
            assert "Test Server" not in self.driver.title
        if scheme == 7:
            assert (
                self.base_page.find(self.registration_page.registration_errors_locators.INCORRECT_EMAIL_LENGTH) and
                self.base_page.find(self.registration_page.registration_errors_locators.INCORRECT_USERNAME_LENGTH) and
                self.base_page.find(self.registration_page.registration_errors_locators.PASSWORDS_MUST_MATCH)
            )
