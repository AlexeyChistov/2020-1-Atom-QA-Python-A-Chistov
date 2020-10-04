"""Тесты для списков"""
import pytest


class TestsForList:

    @pytest.mark.smoke
    def test_append(self, rand_list, rand_int):
        """Проверка метода .append()"""
        rand_list.append(rand_int)
        assert rand_list[len(rand_list) - 1] == rand_int

    @pytest.mark.smoke
    def test_extend(self):
        """Проверка метода .extend()"""
        list_1 = ['Mephi']
        list_2 = ['M', '20', '-', '405']
        list_1.extend(list_2)
        assert list_1 == ['Mephi', 'M', '20', '-', '405']

    def test_insert(self, rand_list):
        """Проверка метода .insert()"""
        list_len = len(rand_list)
        rand_list.insert(1, 'aaa')
        assert rand_list[1] == 'aaa' and len(rand_list) == list_len + 1

    @pytest.mark.parametrize(
        'my_list, count',
        [
            ([1, 1, 1], 3),
            ([1, 1, 0], 2),
            ([1, 0, 0], 1),
        ]
    )
    def test_count(self, my_list, count):
        """Провекрака метода .count()"""
        assert my_list.count(1) == count

    @pytest.mark.parametrize(
        'my_array, sum_of_elements',
        [
            ([1, 2, 3], 6),
            ([4, 5, 6], 15),
            ([7, 8, 9], 24),
        ]
    )
    def test_sum(self, my_array, sum_of_elements):
        """Проверка суммы элементов спика"""
        assert sum(my_array) == sum_of_elements
