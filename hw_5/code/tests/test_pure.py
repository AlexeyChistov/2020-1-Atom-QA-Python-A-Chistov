import pytest
from pure_mysql.pure_mysql_builder import PureMysqlBuilder
from pure_mysql.pure_mysql_client import PureMysqlConnection


class TestPureMysql(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self):
        self.mysql: PureMysqlConnection = PureMysqlConnection()
        self.builder: PureMysqlBuilder = PureMysqlBuilder(self.mysql.table_name)

    def test(self):
        self.mysql.execute_query(self.builder.create_logs_table())
        self.mysql.execute_query(self.builder.insert_log())
        log = self.mysql.execute_query(self.builder.show_table_record())[0]
        assert log['ip'] == self.builder.log['ip']
        assert log['url'] == self.builder.log['url']
