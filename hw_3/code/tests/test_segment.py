from conftest import BaseCase


class TestClass(BaseCase):

    def test_create_segment(self, segment_title):
        """Тестируем создание сегмента"""
        segment_id = self.my_target_client.create_segment(segment_title)
        response = self.my_target_client.checking_segment_creation(segment_id)
        assert response == 200

    def test_create_and_delete_segment(self, segment_title):
        """Тестируем создание и удаление сегиента"""
        segment_id = self.my_target_client.create_segment(segment_title)
        response_create = self.my_target_client.checking_segment_creation(segment_id)
        assert response_create == 200
        response_delete = self.my_target_client.delete_segment(segment_id)
        assert response_delete == 204
