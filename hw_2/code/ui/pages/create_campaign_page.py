from images.banner_path import BannerPath
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.user.data import UserData


class CreateCampaignError(Exception):
    pass


class CreateCampaignPage(BasePage):

    def create_campaign(self, name, created_campaign_xpath):
        self.click(self.create_campaign_locators.CREATE_NEW_CAMPAIGN)
        self.click(self.create_campaign_locators.TRAFFIC_BUTTON)
        self.field_entry(basic_locators.CreateCampaign.CAMPAIGN_LINK, UserData.CAMPAIGN_LINK)
        self.click(self.create_campaign_locators.CAMPAIGN_NAME)
        self.field_entry(self.create_campaign_locators.CAMPAIGN_NAME, f'{name}')
        self.field_entry(self.create_campaign_locators.DAILY_BUDGET, '100')
        self.field_entry(self.create_campaign_locators.TOTAL_BUDGET, '200')
        self.click(basic_locators.CreateCampaign.BANNER_BUTTON)
        self.load_image(self.create_campaign_locators.LOAD_IMAGE_BUTTON, BannerPath.IMAGE_PATH)
        self.click(self.create_campaign_locators.CREATE_NEW_CAMPAIGN)
        self.find(self.main_page_locators.CAMPAIGNS, 10).click()
        return self.find(created_campaign_xpath, 10)

    def check_num_of_created_campaigns(self):
        """Проверяем количество созданных кампаний, если их 30, то вызываем ошибку"""
        if self.find(self.create_campaign_locators.NUM_OF_CAMPAIGNS, 20) is None:
            pass
        else:
            raise CreateCampaignError(
                'Reached limit of created campaigns, delete any campaign to pass the test'
            )
