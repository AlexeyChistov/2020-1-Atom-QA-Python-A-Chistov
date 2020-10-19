import json
import requests
from request_url.request_url import RequestUrl


class ResponseStatusCodeException(Exception):
    pass


class RequestErrorException(Exception):
    pass


class MyTargetClient(RequestUrl):

    def __init__(self, user_mail, user_password):
        self.session = requests.Session()
        self.__user_mail = user_mail
        self.__user_password = user_password
        self.login()
        self.__csrf_token = self.get_token()

    def _request(self, method, url, status_code=200, headers=None, params=None, data=None, json=False):
        response = self.session.request(method, url, headers=headers, params=params, data=data)
        if response.status_code != status_code:
            raise ResponseStatusCodeException(f' Got {response.status_code} {response.reason} for URL "{url}"')
        if json is True:
            json_response = response.json()
            if json_response.get('error'):
                err = json_response['error']['code']
                mess = json_response['error']['message']
                raise RequestErrorException(f'Request url: "{url}", error: "{err}", message: "{mess}"!')
            return json_response
        return response

    def login(self):
        """Авторизуемся"""
        url = self.get_login_url()
        headers = {
            'referer': 'https://target.my.com/'
        }

        data = {
            'email': self.__user_mail,
            'password': self.__user_password,
            'continue': 'https://target.my.com/auth/mycom?state=target_login',
            'failure': 'https://account.my.com/login/'
        }

        response = self._request('POST', url, headers=headers, data=data)
        return response

    def get_token(self):
        """Получаем токен из кук (после корректной авторизации)"""
        url = self.get_csrf_token_url()
        response = self._request('GET', url)
        return response.cookies['csrftoken']

    def create_segment(self, segment_title):
        """Создаем сегмент"""
        url = self.get_create_segment_url()
        headers = {
            'x-csrftoken': self.__csrf_token
        }
        data = json.dumps({
            'name': f'{segment_title}',
            'pass_condition': 1,
            'relations': [
                {
                    'object_type': 'remarketing_player',
                    'params': {
                        'type': 'positive',
                        'left': 365,
                        'right': 0
                    }
                }
            ],
            'logicType': 'or'
        })

        response = self._request('POST', url, headers=headers, data=data, json=True)['id']
        return response

    def checking_segment_creation(self, segment_id):
        """Проверяем по id, что сегмент создался"""
        url = self.get_segments_url(segment_id)
        try:
            response = self._request('GET', url, status_code=200)
            print(f'Сегмент с id:{segment_id} успешно создан')
            return response.status_code
        except Exception:
            raise

    def delete_segment(self, segment_id):
        """Удаляем сегмент по id"""
        url = self.get_delete_segment_url(segment_id)
        headers = {
            'x-csrftoken': self.__csrf_token
        }
        response = self._request('DELETE', url, headers=headers, status_code=204)
        return response.status_code
