"""Тут разбиваем локаторы на классы, в соответсвием их местоположением на странице"""

from selenium.webdriver.common.by import By


class BasePageLocators(object):
    """
    Локаторы страницы с формой авторизации (base, welcome)
    """
    UK_CARD_TITLE = (By.XPATH, '//h3[contains(text(), "Welcome")]')
    USERNAME_FIELD = (By.XPATH, '//input[@name="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[contains(@class, "uk-button")]')
    CREATE_AN_ACCOUNT_BUTTON = (By.XPATH, '//a[contains(text(), "Create an account")]')


class RegistrationFormLocators(object):
    """
    Локаторы странички с формой регистрации
    P.S. локаторы для username и password такие же, как и в классе base/welcome
    Необходимо в тестах проверять еще и title формы
    """
    UK_CARD_TITLE = (By.XPATH, '//h3[contains(text(), "Registration")]')
    USERNAME_FIELD = (By.XPATH, '//input[@name="username"]')
    EMAIL_FIELD = (By.XPATH, '//input[@name="email"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    REPEAT_PASSWORD_FIELD = (By.XPATH, '//input[@placeholder="Repeat password"]')
    ACCEPT_FLAG = (By.XPATH, '//input[@type="checkbox"]')
    REGISTER_BUTTON = (By.XPATH, '//input[@value="Register"]')
    LOG_IN = (By.XPATH, '//a[contains(text(), "Log in")]')


class MainPageLocators:
    """Элементы главной страницы"""
    HOME_BUTTON = (By.XPATH, '//a[contains(text(), "HOME")]')

    PYTHON = (By.XPATH, '//a[@href="https://www.python.org/"]')
    PYTHON_OPEN_STATUS = (By.XPATH, '//nav[@class="uk-navbar"]/ul/li[2][contains(@class, "uk-open")]')
    PYTHON_HISTORY = (By.XPATH, '//a[contains(@href, "/History_of_Python")]')
    ABOUT_FLASK = (By.XPATH, '//a[contains(text(), "About Flask")]')

    LINUX = (By.XPATH, '//a[contains(text(), "Linux")]')
    LINUX_BUTTON_OPEN_STATUS = (By.XPATH, '//nav[@class="uk-navbar"]/ul/li[3][contains(@class, "uk-open")]')
    DOWNLOAD_CENTOS_7 = (By.XPATH, '//a[contains(text(), "Centos")]')

    NETWORK = (By.XPATH, '//a[contains(text(), "Network")]')
    NETWORK_BUTTON_OPEN_STATUS = (By.XPATH, '//nav[@class="uk-navbar"]/ul/li[4][contains(@class, "uk-open")]')
    WIRESHARK_NEWS = (By.XPATH, '//a[contains(@href, ".wireshark.org/news")]')
    WIRESHARK_DOWNLOAD = (By.XPATH, '//a[contains(@href, ".wireshark.org/#download")]')
    TCPDUMP_EXAMPLES = (By.XPATH, '//a[contains(text(), "Examples")]')

    # Animated buttons
    WHAT_IS_AN_API = (By.XPATH, '//img[contains(@src, "/laptop")]')
    FUTURE_OF_INTERNET = (By.XPATH, '//img[contains(@src, "/loupe")]')
    LETS_TALK_ABOUT_SMTP = (By.XPATH, '//img[contains(@src, "/analytics")]')

    # static elements
    PANEL = (By.XPATH, '//*[@id="wrap"]/header/nav')
    VK_ID = (By.XPATH, '//li[contains(text(), "VK ID")]')
    LOG_OUT = (By.XPATH, '//li[contains(text(), "Logout")]')
    LOGGED_AS = (By.XPATH, '//li[contains(text(), "Logged as")]')


class AuthorizationFormErrorsLocators(object):
    """Ошибки, всплывающие при заполнении формы авторизации"""
    INVALID_USERNAME_OR_PASSWORD = (
        By.XPATH, '//div[contains(text(), "Invalid") and not(contains(@style, "hidden"))]'
    )


class RegistrationFormErrorsLocators(object):
    """Ошибки, всплывающие при заполнении формы регистрации"""
    INCORRECT_USERNAME_LENGTH = (
        By.XPATH, '//div[contains(text(), "Incorrect username length") and not(contains(@style, "hidden"))]'
    )

    INCORRECT_EMAIL_LENGTH = (
        By.XPATH, '//div[contains(text(), "Incorrect email length") and not(contains(@style, "hidden"))]'
    )

    PASSWORDS_MUST_MATCH = (
        By.XPATH, '//div[contains(text(), "Passwords must match") and not(contains(@style, "hidden"))]'
    )

    INVALID_EMAIL_ADDRESS = (
        By.XPATH, '//div[contains(text(), "Invalid email address") and not(contains(@style, "hidden"))]'
    )

    INTERNAL_SERVER_ERROR = (
        By.XPATH, '//div[contains(text(), "Internal Server Error") and not(contains(@style, "hidden"))]'
    )

    # ожидаем скрытый алерт
    USER_ALREADY_EXISTS = (
        By.XPATH, '//div[contains(text(), "User already exists") and not(contains(@style, "hidden"))]'
    )

