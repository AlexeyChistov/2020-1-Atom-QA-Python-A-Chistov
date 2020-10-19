import pytest
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType

from ui.pages.base_page import BasePage
from ui.pages.create_campaign_page import CreateCampaignPage
from ui.pages.create_segment_page import CreateSegmentPage
from ui.pages.login_page import LoginPage
from ui.user.data import UserData


def pytest_addoption(parser):
    """Как понятно из названия инициалтзируем дефолтные браузер, версию и урл"""
    parser.addoption("--url", default='https://target.my.com/')
    parser.addoption("--browser", default='chrome')
    parser.addoption("--browser_ver", default='latest')
    parser.addoption("--selenoid", default=None)


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption("--browser")
    version = request.config.getoption("--browser_ver")
    url = request.config.getoption("--url")
    selenoid = request.config.getoption("--selenoid")
    return {
        'browser': browser,
        'version': version,
        'url': url,
        'selenoid': selenoid
    }


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def create_campaign_page(driver):
    return CreateCampaignPage(driver=driver)


@pytest.fixture
def create_segment_page(driver):
    return CreateSegmentPage(driver=driver)


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = config['browser']
    version = config['version']
    selenoid = config['selenoid']

    if selenoid:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "80.0",
            "selenoid:options": {
                "enableVNC": False,
                "enableVideo": False
            }
        }
        driver = webdriver.Remote(
            command_executor=f'http://{selenoid}/wd/hub',
            desired_capabilities=capabilities
        )
    else:
        if browser == 'chrome':
            manager = ChromeDriverManager(version=version, log_level=0)
            driver = webdriver.Chrome(manager.install())
        elif browser == 'firefox':
            manager = GeckoDriverManager(version=version, log_level=0)
            driver = webdriver.Firefox(executable_path=manager.install())
        else:
            raise Exception
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def auto_auth(request: FixtureRequest):
    login_page: LoginPage = request.getfixturevalue('login_page')
    return login_page.login_success(UserData.USER_MAIL, UserData.USER_PASS)
