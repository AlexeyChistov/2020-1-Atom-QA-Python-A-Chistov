"""Тесты для строк"""
import pytest


class TestsForStr:

    @pytest.mark.smoke
    def test_concatenation(self):
        """Провекрка конкатенации строк"""
        string_1 = 'qwe'
        string_2 = 'rty'
        assert string_1 + string_2 == 'qwerty'

    @pytest.mark.smoke
    def test_multi(self):
        """Проверка дублирования строки"""
        my_string = 'Ok'
        assert my_string * 4 == 'OkOkOkOk'

    def test_islower(self, rand_str):
        """Проверка, что случайная строка в нижнем регистре"""
        print(rand_str)
        assert rand_str.islower() is True

    @pytest.mark.parametrize(
        'my_string, capitalized_string',
        [
            ('HELLO world', 'Hello world'),
            ('heLLO woRlD', 'Hello world'),
            ('Hello world', 'Hello world')
        ]
    )
    def test_capitalize(self, my_string, capitalized_string):
        """Проверка .capitalize()"""
        my_string = my_string.capitalize()
        assert my_string == capitalized_string

    @pytest.mark.parametrize(
        'my_string, new_string',
        [
            ('  qwe', 'qwe'),
            ('rty    ', 'rty'),
            ('   uio ', 'uio')
        ]
    )
    def test_strip(self, my_string, new_string):
        """Проверка на удаление пробельных символов в начале и конце"""
        my_string = my_string.strip()
        assert my_string == new_string
