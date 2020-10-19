import pytest
import datetime
from _pytest.fixtures import FixtureRequest
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.pages.create_campaign_page import CreateCampaignPage
from ui.pages.create_segment_page import CreateSegmentPage
from ui.pages.login_page import LoginPage
from ui.locators import basic_locators
from ui.user.data import UserData


class BaseCase:
    """Наш автоюз"""
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.create_campaign_page: CreateCampaignPage = request.getfixturevalue('create_campaign_page')
        self.create_segment_page: CreateSegmentPage = request.getfixturevalue('create_segment_page')
        self.login_page: LoginPage = request.getfixturevalue('login_page')

    @pytest.fixture(scope='function')
    def name_and_xpath(self):
        """Генерируем имя с помощью метода datetime """
        time = datetime.datetime.now()
        segment_title = f'Тестовый сегмент от {time}'
        campaign_title = f'Тестовая кампания от {time}'
        created_segment_xpath = (By.XPATH, f'//*[contains(text(), "{segment_title}")]')
        created_campaign_xpath = (By.XPATH, f'//*[contains(text(), "{campaign_title}")]')
        delete_segment_cross_xpath = (
            By.XPATH, f'//a[contains(text(), "{time}")]/ancestor::div[contains(@role, "rowgroup")]/descendant::span[2]'
        )
        data = {
            'segment_title': segment_title,
            'campaign_title': campaign_title,
            'created_campaign_xpath': created_campaign_xpath,
            'created_segment_xpath': created_segment_xpath,
            'delete_segment_cross_xpath': delete_segment_cross_xpath
        }
        return data
