"""Тесты для словарей"""
import pytest


class TestsForDict:

    @pytest.mark.smoke
    def test_clear(self, rand_dict):
        """Проверка метода .clear()"""
        rand_dict.clear()
        assert rand_dict == {}

    @pytest.mark.smoke
    def test_wrong_key(self):
        """Проверка получения значения по несуществующему ключу"""
        my_dict = {
            'key_1': 'value_1',
            'key_2': 'value_2'
        }
        with pytest.raises(KeyError):
            assert my_dict['key_3']

    def test_update(self):
        """Тест для метода .update()"""
        my_dict_1 = {
            'key_1': 'value_1'
        }
        my_dict_2 = {
            'key_2': 'value_2'
        }
        my_dict_1.update(my_dict_2)
        assert my_dict_1 == {'key_1': 'value_1', 'key_2': 'value_2'}

    def test_add_key(self, rand_dict):
        """Проверка добавления добавления нового ключа в случайный словарь"""
        rand_dict['year'] = 2020
        assert rand_dict['year'] == 2020

    @pytest.mark.parametrize(
        'my_dict, key_pop, new_dict',
        [
            ({'key_1': 'value_1', 'key_2': 'value_2'}, 'key_2', {'key_1': 'value_1'}),
            ({'key_1': 'value_1'}, 'key_1', {})
        ]
    )
    def test_pop(self, my_dict, key_pop, new_dict):
        """Проверка того, что .pop() удаляет ключ и соответствующее значение из словаря"""
        my_dict.pop(key_pop)
        assert my_dict == new_dict
