from urllib.parse import urljoin


class Config:
    APP_HOST, APP_PORT = '127.0.0.1', 1234
    APP_URL = f'http://{APP_HOST}:{APP_PORT}'

    MOCK_HOST, MOCK_PORT = '127.0.0.1', 5678
    MOCK_URL = f'http://{MOCK_HOST}:{MOCK_PORT}'
    MOCK_USER_URL = urljoin(MOCK_URL, '')
