from fixtures.base import BaseCase
import pytest


class TestCampaign(BaseCase):
    @pytest.mark.UI
    def test_create_campaign(self, auto_auth, name_and_xpath):
        """Тест на создание кампании"""
        self.create_campaign_page.check_num_of_created_campaigns()
        assert self.create_campaign_page.create_campaign(
            name_and_xpath['campaign_title'], name_and_xpath['created_campaign_xpath']
        )

