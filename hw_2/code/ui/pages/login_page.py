from ui.pages.base_page import BasePage


class LoginPage(BasePage):
    def login_success(self, mail, password):
        """Успешная авторизация"""
        self.click(self.base_page_locators.LOG_IN)
        self.entering_email_and_password(mail, password)
        self.find(self.main_page_locators.CAMPAIGNS)
        return self.find(self.main_page_locators.CAMPAIGNS)

    def login_failed(self, mail, password):
        """Авторизация с ошибкой"""
        self.click(self.base_page_locators.LOG_IN)
        self.entering_email_and_password(mail, password)
        return self.find(self.login_page_locators.LOG_IN_FAILED)
