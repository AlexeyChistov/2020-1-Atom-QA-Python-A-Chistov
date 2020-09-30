"""Тесты для множеств"""
import pytest


class TestsForList:

    def test_clear(self, rand_set):
        """Проверка метода .clear()"""
        rand_set.clear()
        assert rand_set == set([])

    def test_update(self):
        """Проверка метода .update"""
        set_1 = {1, 2, 3, 4}
        set_2 = {5, 6, 7, 8}
        set_1.update(set_2)
        assert set_1 == {1, 2, 3, 4, 5, 6, 7, 8}

    def test_remove(self):
        """Проверка метода .remove()"""
        my_set = {2, 4, 6, 8}
        my_set.remove(2)
        assert my_set == {4, 6, 8}

    def test_add(self):
        """Проверка метода .add()"""
        my_set = {1, 2, 3, 4}
        my_set.add(5)
        assert my_set == {1, 2, 3, 4, 5}

    @pytest.mark.parametrize(
        'my_set, elem, new_set',
        [
            ({1, 2, 3}, 1, {2, 3}),
            ({4, 5, 6}, 5, {4, 6}),
            ({7, 8, 9}, 9, {7, 8}),
        ]
    )
    def test_discard(self, my_set, elem, new_set):
        """Провекрака метода .discard()"""
        my_set.discard(elem)
        assert my_set == new_set
