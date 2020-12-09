import json

import pytest

from fixtures.base_case_api import BaseCaseApi


class TestCheck(BaseCaseApi):

    @pytest.mark.API
    def test_check_status_pos_1(self):
        """Позитив тест на проверку статуса приложения"""
        response = self.api_page.app_status()
        assert response.status_code == 200
        assert json.loads(response.text) == {"status": "ok"}

    @pytest.mark.API_401
    def test_check_status_pos_2(self):
        """
        Запрос статуса
        """
        response = self.api_page_401.app_status()
        assert response.status_code == 200
