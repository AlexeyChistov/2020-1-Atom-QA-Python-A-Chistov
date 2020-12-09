import pytest
from fixtures.base_case_ui import BaseCaseUi
from random import choice
import string

from test_data import ui_main_page_data
from UI.ui_exceptions.exceptions import WrongResource, ButtonRedirectError

print(''.join(choice(string.digits + string.ascii_letters) for i in range(25)))


class TestMainPage(BaseCaseUi):

    @pytest.mark.skip(reason="no need")
    @pytest.mark.UI
    @pytest.mark.parametrize("locator_1, locator_2, expected_title", ui_main_page_data.PARAMS_FOR_GO_TO)
    def test_go_to(self, auto_auth, locator_1, locator_2, expected_title):
        """
        Нажимаем на кнопку главной странички для перехода на соответствующий ресурс
        Ожидаемое поведение: при нажатии на вкладку открывает новое окно, конопка должна вести в корректный ресурс
        (идет проверка с тайтлом), также не должно открываться лишних вкладок

        Чтобы получить тайтл новой вкладки, необходимо выполнить switch_to
        Проверяем, что при нажатии на ссылку, в браузере открыто только 2 окна
        """
        try:
            new_window_title, previous_window_title, number_of_windows = self.main_page.go_to(locator_1, locator_2)
        except ValueError:
            raise ButtonRedirectError(f"Button with locator: '{locator_2}' unexpected behavior!")
        try:
            assert expected_title in new_window_title
        except AssertionError:
            raise WrongResource(f"Incorrect resource window, expected title: {expected_title}")
        assert number_of_windows == 2 and "Test Server" in previous_window_title

    @pytest.mark.UI
    @pytest.mark.parametrize("interactive_buttons", ui_main_page_data.MAIN_PAGE_INTERACTIVE_BUTTONS_LIST)
    def test_cursor_type(self, auto_auth, interactive_buttons):
        """
        Тестируем смену стрелки на палец при наведении на соответсвтвующие объекты
        """
        print("a", interactive_buttons)
        cursor_type = self.main_page.check_cursor_type(interactive_buttons)
        assert cursor_type == "pointer"

    @pytest.mark.UI
    @pytest.mark.parametrize("master_button, slaves_buttons", ui_main_page_data.PARAMS_FOR_TEST_ACCORDION_BUTTONS)
    def test_accordion_positive(self, auto_auth, master_button, slaves_buttons):
        """
        Позитивный тест
        Тестируем, что при наведении на аккордион, скрытые кнопки становятся активными
        """
        self.base_page.move_to_element(master_button)
        for button in slaves_buttons:
            assert self.base_page.find(button).is_displayed()

    @pytest.mark.UI
    @pytest.mark.parametrize("master_button, slaves_buttons", ui_main_page_data.PARAMS_FOR_TEST_ACCORDION_BUTTONS)
    def test_accordion_negative(self, auto_auth, master_button, slaves_buttons):
        """
        Негативный тест
        Тестируем, что без наведения на аккордион, скрытые кнопки не активны
        """
        for button in slaves_buttons:
            assert self.base_page.find(button).is_displayed() is False
