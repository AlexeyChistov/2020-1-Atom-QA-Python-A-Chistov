import pytest
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType


def pytest_addoption(parser):
    """Как понятно из названия инициалтзируем дефолтные браузер, версию и урл"""
    parser.addoption("--url", default='http://myapp:8081/')
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


@pytest.fixture(scope='function')
def driver(config):
    url = config['url']
    browser = config['browser']
    version = config['version']
    selenoid = config['selenoid']

    if selenoid:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "87.0",
            "selenoid:options": {
                "enableVNC": True,
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
            driver = webdriver.Chrome(executable_path=manager.install())
        elif browser == 'firefox':
            manager = GeckoDriverManager(version=version, log_level=0)
            driver = webdriver.Firefox(executable_path=manager.install())
        else:
            raise Exception

    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()
