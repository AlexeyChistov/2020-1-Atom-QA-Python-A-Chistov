import pytest

from fixtures.base_case_api import BaseCaseApi


class TestDel(BaseCaseApi):

    @pytest.mark.API
    def test_dell_user_pos_1(self):
        """Позитив тест на удаление"""
        self.api_page.add_user("Alexey", "123", "aa.@aa.aa")
        response = self.api_page.delete_user("Alexey")
        assert response.status_code == 204

    @pytest.mark.API
    def test_dell_user_pos_2(self):
        """Позитив тест на удаление"""
        self.api_page.add_user("Alexey", "123", "aa.@aa.aa")
        self.api_page.delete_user("Alexey")
        response_from_table = self.api_page.check_user("Alexey")
        assert response_from_table.status_code == 404

    @pytest.mark.API
    def test_dell_user_neg_1(self):
        """
        Негатив тест на удаление
        Пытаемся удалить удаленного/несуществующего пользователя
        """
        self.api_page.add_user("Alexey", "123", "aa.@aa.aa")
        self.api_page.delete_user("Alexey")
        response = self.api_page.delete_user("Alexey")
        assert response.status_code == 404

    @pytest.mark.API_401
    def test_dell_user_neg_2(self):
        """
        Негатив тест на 401
        """
        self.api_page_401.add_user("Alexey", "123", "aa.@aa.aa")
        self.api_page_401.delete_user("Alexey")
        response = self.api_page_401.delete_user("Alexey")
        assert response.status_code == 401
