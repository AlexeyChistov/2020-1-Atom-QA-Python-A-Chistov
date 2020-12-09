import json
import requests

from API.endpoints import RoutesForApi

#todo организовать все по-другому (например добавить ультротестового бифкейк юзера, который добавляется при поднятии
# db контейнера и закинуть уго в тест дату
from test_data import users


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class ApiClient(RoutesForApi):
    TEST_USER = users.SUPER_USER_KEYS[0]
    TEST_PASSWORD = password = users.SUPER_USER[f"{TEST_USER}"][0]

    def __init__(self, auto_authorize=True):
        """
        Необходимо авторизовываться под каким-нибудь юзером, чтобы работали api запросы
        Если в клас не передается False, то происходит автоматическая авторизация
        (без этого API запросы будут выплевывать 401)
        """
        self.session = requests.Session()
        if auto_authorize:
            self.auth_user()

    def auth_user(self):
        url = self.auth_user_url()
        """Авторизуемся под тестовым юзером"""
        data = {
            "username": self.TEST_USER,
            "password": self.TEST_PASSWORD
        }
        self._request('POST', url, data=data)

    def _request(self, method, url, expected_status_code=200, headers=None, params=None, data=None, json=False):
        """Мой реквест, основанный на session.request"""

        response = self.session.request(
            method,
            url,
            headers=headers,
            params=params,
            data=data
        )
        return response

    def app_status(self, expected_status_code=200):
        url = self.app_status_url()
        response = self._request('GET', url, expected_status_code=expected_status_code)
        return response

    def add_user(self, username, password, email, expected_status_code=200):
        """Добавляем пользователя"""
        url = self.add_user_url()
        headers = {
            "content-type": "application/json",

        }
        data = json.dumps({
            "username": f"{username}",
            "password": f"{password}",
            "email": f"{email}"
        })
        response = self._request('POST', url, headers=headers, data=data, expected_status_code=expected_status_code)
        return response

    def delete_user(self, username, expected_status_code=200):
        """Удаляем пользователя"""
        url = self.del_user_url(username)
        response = self._request('GET', url, expected_status_code=expected_status_code)
        return response

    def block_user(self, username, expected_status_code=200):
        """Удаляем пользователя"""
        url = self.block_user_url(username)
        response = self._request('GET', url, expected_status_code=expected_status_code)
        return response

    def accept_user(self, username, expected_status_code=200):
        """Удаляем пользователя"""
        url = self.accept_user_url(username)
        response = self._request('GET', url, expected_status_code=expected_status_code)
        return response

    def check_user(self, username, expected_status_code=200):
        """Получаем всю информацию о пользователе, если он добавлен в БД"""
        url = self.user_info(username)
        response = self._request('GET', url, expected_status_code=expected_status_code)
        return response
