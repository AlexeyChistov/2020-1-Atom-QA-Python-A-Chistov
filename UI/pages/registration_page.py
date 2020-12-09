from UI.locators import locators
from UI.pages.base_page import BasePage


# todo написать эсэпшены на все случаи жизни
# class CreateCampaignError(Exception):
#     pass


class RegistrationPage(BasePage):
    """Страница формы регистрации"""
    # todo либо так, либо все локаторы описать в BasePage
    registration_page_locators = locators.RegistrationFormLocators()
    registration_errors_locators = locators.RegistrationFormErrorsLocators()

    def user_registration(self, username, email, password, password_accepting, accept_flag=None):
        self.click(self.base_page_locators.CREATE_AN_ACCOUNT_BUTTON)
        self.field_entry(self.registration_page_locators.USERNAME_FIELD, username)
        self.field_entry(self.registration_page_locators.EMAIL_FIELD, email)
        self.field_entry(self.registration_page_locators.PASSWORD_FIELD, password)
        self.field_entry(self.registration_page_locators.REPEAT_PASSWORD_FIELD, password_accepting)
        if accept_flag:
            self.click(self.registration_page_locators.ACCEPT_FLAG)
        self.click(self.registration_page_locators.REGISTER_BUTTON)
