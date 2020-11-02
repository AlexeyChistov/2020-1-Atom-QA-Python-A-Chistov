from my_parser.log_parser import DATA_FRAMES
from my_parser.load_logs_mysql_client import MysqlOrmConnection


class MysqlOrmBuilder(object):
    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = self.connection.connection.engine

    def write_table(self):
        for df_key in DATA_FRAMES:
            if not self.engine.dialect.has_table(self.engine, f'{df_key}'):
                DATA_FRAMES[df_key].to_sql(name=f'{df_key}', con=self.engine)
