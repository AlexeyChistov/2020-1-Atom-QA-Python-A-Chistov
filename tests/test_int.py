"""Тесты для int"""
import pytest


class TestsForInt:

    @pytest.mark.smoke
    def test_div_by_zero(self, rand_int):
        """Проверка деления на ноль"""
        with pytest.raises(ZeroDivisionError):
            assert rand_int / 0

    @pytest.mark.smoke
    def test_int_div(self):
        """Проверка на целочисленного деление"""
        assert 5 // 2 == 2

    def test_div_rem(self):
        """Проверка на деление с остатком"""
        assert 5 % 2 == 1

    @pytest.mark.parametrize(
        'neg_num, pos_num, abs_num ',
        [
            (0, 0, 0),
            (-2, 2, 2),
            (-4, 4, 4),
            (-8, 8, 8),
        ],
    )
    def test_abs(self, neg_num, pos_num, abs_num):
        """Проверка модуля числа"""
        assert (abs(neg_num) == abs_num) and (abs(pos_num) == abs_num)

    @pytest.mark.parametrize(
        'neg_num, abs_num, sqr_num ',
        [
            (0, 0, 0),
            (-2, 2, 4),
            (-4, 4, 16),
            (-8, 8, 64),
        ],
    )
    def test_sqr(self, neg_num, abs_num, sqr_num):
        """Проверка возведения в квадрат"""
        assert (neg_num ** 2 == sqr_num) and (abs_num ** 2 == sqr_num)
