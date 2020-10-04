"""Фикстуры"""
import pytest
import string
import random


@pytest.fixture(scope='class')
def rand_int():
    """Случайное число"""
    return random.randint(-1000, 1000)


@pytest.fixture(scope='function')
def rand_list():
    """Случайный список из чисел"""
    return [random.randint(-1000, 1000) for i in range(2, 20)]


@pytest.fixture(scope='class')
def rand_set():
    """Случайное множество"""
    return {random.randint(-1000, 1000) for i in range(2, 20)}


@pytest.fixture(scope='function')
def rand_dict():
    """Случайный словарь"""
    return {'key_' + str(x): 'value_' + str(x) for x in range(random.randint(2, 20))}


@pytest.fixture(scope='class')
def rand_str():
    """Случайная строка нижнего регистра"""
    letters = string.ascii_lowercase
    new_str = ''.join(random.choice(letters) for x in range(random.randint(2, 20)))
    return new_str
