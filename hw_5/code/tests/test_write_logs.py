import pytest
from my_parser.load_logs_mysql_client import MysqlOrmConnection
from my_parser.load_logs_builder import MysqlOrmBuilder


class TestMysqlOrm(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.mysql: MysqlOrmConnection = MysqlOrmConnection()
        self.builder: MysqlOrmBuilder = MysqlOrmBuilder(connection=self.mysql)

    def test(self):
        self.builder.write_table()
