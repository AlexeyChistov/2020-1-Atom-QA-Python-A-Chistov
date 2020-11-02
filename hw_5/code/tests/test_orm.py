import random
import pytest
from faker import Faker
from log_maker.log_maker import LogMaker
from orm_mysql.models.orm_model import Model
from orm_mysql.orm_mysql_builder import OrmSqlBuilder
from orm_mysql.orm_mysql_client import OrmMysqlConnection


class TestOrmMysql:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.orm_sql = OrmMysqlConnection()
        self.builder: OrmSqlBuilder = self.orm_sql.builder
        self.fake_log: LogMaker = LogMaker()

    def test(self):
        fake = Faker()
        fake_log = Model(
            ip=fake.ipv4(),
            date=fake.date(),
            method=fake.http_method(),
            url=fake.url(),
            resp_code=random.choice([200, 300, 302, 401, 402, 403, 404, 500, 501, 666])
        )
        print(fake_log)

        self.builder.create_log_table()
        self.builder.insert_log(fake_log)

        log_inserted = self.builder.show_log()[0]
        print(log_inserted)
        assert log_inserted == fake_log
