from fixtures.base import BaseCase
import pytest


class TestSegment(BaseCase):
    @pytest.mark.UI
    def test_create_segment(self, auto_auth, name_and_xpath):
        """Создаем сегмент, и проверяем, что он создан"""
        assert self.create_segment_page.create_segment(
            name_and_xpath['segment_title'], name_and_xpath['created_segment_xpath']
        )

    @pytest.mark.UI
    def test_create_and_delete_segment(self, auto_auth, name_and_xpath):
        """Создаем сегмент, проверяем, что он создан, удаляем сегмент и проверяем, что сегмент удален"""
        name = name_and_xpath['segment_title']
        xpath = name_and_xpath['created_segment_xpath']
        cross_xpath = name_and_xpath['delete_segment_cross_xpath']
        self.create_segment_page.create_segment(name, xpath)
        assert self.create_segment_page.delete_segment(cross_xpath) is None
