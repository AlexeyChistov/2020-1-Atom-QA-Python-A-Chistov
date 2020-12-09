"""
Фикстуры для класса Base
Нужно для:
self.base_page: BasePage = request.getfixturevalue('base_page')
"""
import pytest

from UI.pages.base_page import BasePage
from UI.pages.main_page import MainPage
from UI.pages.registration_page import RegistrationPage


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver=driver)


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)

