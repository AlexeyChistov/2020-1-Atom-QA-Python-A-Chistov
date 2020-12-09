from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from UI.locators import locators


class BasePage(object):
    """Страничка с формой авторизации"""
    base_page_locators = locators.BasePageLocators()
    authorization_errors_locators = locators.AuthorizationFormErrorsLocators()

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def find(self, locator, timeout=None) -> WebElement:
        """Находим элемент, ожидаем до тех пор, пока он не появится"""
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def check_clickable(self, locator, timeout=None) -> WebElement:
        """Проверяем элемент на кликабильность"""
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        """Кликаем на элемент"""
        try:
            self.find(locator)
            element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception:
            raise

    def wait(self, timeout=None):
        """Таймаут"""
        if timeout is None:
            timeout = 15
        return WebDriverWait(self.driver, timeout=timeout)

    def field_entry(self, locator, keys):
        """Ввод в поле ввода соответствующего локатора"""
        field = self.find(locator)
        field.clear()
        field.send_keys(keys)

    def move_to_element(self, locator):
        """Наводимся на элемент"""
        element = self.find(locator)
        print("tut", element)
        self.action.move_to_element(element).perform()
        self.wait(0.5)

    def login_1(self, username, password):
        """Ввод: email -> password -> Enter (в поле password) """
        self.field_entry(self.base_page_locators.USERNAME_FIELD, username)
        self.field_entry(self.base_page_locators.PASSWORD_FIELD, password)
        self.find(self.base_page_locators.PASSWORD_FIELD).send_keys(Keys.RETURN)

    def login_2(self, username, password):
        """Ввод: email -> password -> Enter (в поле email) """
        self.field_entry(self.base_page_locators.USERNAME_FIELD, username)
        self.field_entry(self.base_page_locators.PASSWORD_FIELD, password)
        self.find(self.base_page_locators.USERNAME_FIELD).send_keys(Keys.RETURN)

    def login_3(self, username, password):
        """Ввод: email -> password -> кнопка Login """
        self.field_entry(self.base_page_locators.USERNAME_FIELD, username)
        self.field_entry(self.base_page_locators.PASSWORD_FIELD, password)
        self.click(self.base_page_locators.LOGIN_BUTTON)
