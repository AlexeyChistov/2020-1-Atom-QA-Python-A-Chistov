import pytest


from api.mytarget_client import MyTargetClient
from data.user_data import UserData
import datetime


class BaseCase:
    """Авторизация"""
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.my_target_client = MyTargetClient(UserData.USER_MAIL, UserData.USER_PASSWORD)

    @pytest.fixture(scope='function')
    def segment_title(self):
        """Генерируем имя сегмента с помощью метода datetime """
        time = datetime.datetime.now()
        segment_title = f'Тестовый сегмент от {time}'
        return segment_title
