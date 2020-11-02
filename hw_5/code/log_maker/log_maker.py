from faker import Faker
import random


class LogMaker:

    def fake_logger(self):
        fake = Faker()
        fake_log = {
            'ip': fake.ipv4(),
            'date': fake.date(),
            'method': fake.http_method(),
            'url': fake.url(),
            'resp_code': random.choice([200, 300, 302, 401, 402, 403, 404, 500, 501, 666])
        }
        return fake_log
