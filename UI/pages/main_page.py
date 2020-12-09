from UI.locators import locators
from UI.pages.base_page import BasePage


# todo написать эсэпшены на все случаи жизни
# class CreateCampaignError(Exception):
#     pass


class MainPage(BasePage):
    """Главная страница сайта"""
    # todo либо так, либо все локаторы описать в BasePage
    main_page_locators = locators.MainPageLocators()

    def go_to(self, locator_1, locator_2):
        """Наводимся на аккордион, после чего всплывают скрытые кнопки"""
        self.move_to_element(locator_1)
        self.click(locator_2)
        app_window, new_window = self.driver.window_handles
        number_of_windows = len(self.driver.window_handles)
        self.driver.switch_to.window(new_window)
        new_window_title = self.driver.title
        self.driver.switch_to.window(app_window)
        previous_window_title = self.driver.title
        return new_window_title, previous_window_title, number_of_windows

    def check_cursor_type(self, locator):
        cursor_type = self.find(locator).value_of_css_property("cursor")
        return cursor_type
