from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ui.locators import basic_locators



class BasePage(object):
    main_page_locators = basic_locators.MainPageLocators()
    base_page_locators = basic_locators.BasePageLocators()
    login_page_locators = basic_locators.LoginLocators()
    create_campaign_locators = basic_locators.CreateCampaign()
    create_segment_locators = basic_locators.CreateSegment()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None):
        """Находим элемент"""
        try:
            return self.wait(timeout).until(EC.presence_of_element_located(locator))
        except Exception:
            return None

    def click(self, locator, timeout=None):
        try:
            self.find(locator)
            element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception:
            raise

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def field_entry(self, locator, keys):
        """Ввод в поле ввода соответствующего локатора"""
        field = self.find(locator)
        field.clear()
        field.send_keys(keys)

    def load_image(self, locator, image_path):
        """Загрузка изображения с компа"""
        image_field = self.find(locator)
        image_field.send_keys(image_path)

    def entering_email_and_password(self, email, password):
        """Ввод: email -> password -> Enter """
        self.field_entry(self.login_page_locators.LOG_IN_EMAIL, email)
        self.field_entry(self.login_page_locators.LOG_IN_PASSWORD, password)
        self.find(self.login_page_locators.LOG_IN_PASSWORD).send_keys(Keys.RETURN)
