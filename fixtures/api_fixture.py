import pytest

from API.api_client import ApiClient
from test_data import users
from test_data.data_generator import DataGenerator
admin = users.SUPER_USER_KEYS[0]
password = users.SUPER_USER[f"{admin}"][0]


@pytest.fixture
def api_page():
    return ApiClient(admin=admin, password=password)


@pytest.fixture
def api_page_401():
    return ApiClient(False)


@pytest.fixture
def generator():
    return DataGenerator()
