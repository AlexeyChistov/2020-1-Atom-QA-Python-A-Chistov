from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config
from log_maker.log_maker import LogMaker
from orm_mysql.orm_mysql_builder import OrmSqlBuilder


class OrmMysqlConnection(LogMaker):
    def __init__(self):
        config: Config = Config()
        self.user = config.USER
        self.password = config.PASSWORD
        self.db_name = config.ORM_SQL_DB_NAME
        self.table_name = config.ORM_SQL_TABLE_NAME
        self.port = config.PORT
        self.host = config.HOST
        self.connection = self.connect()
        session = sessionmaker(bind=self.connection)
        self.session = session()
        self.builder = OrmSqlBuilder(connection=self.connection, session=self.session,
                                     table_name=self.table_name)
        # self.builder.create_log_table()
        self.fake_log = self.fake_logger()

    def connect(self):
        connection = self.get_connection(is_db_created=False)
        connection.execute(f'DROP DATABASE IF EXISTS `{self.db_name}`')
        connection.execute(f'CREATE DATABASE IF NOT EXISTS `{self.db_name}`')
        connection.close()

        return self.get_connection(is_db_created=True)

    def get_connection(self, is_db_created=False):
        engine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'.format(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            db_name=self.db_name if is_db_created else ''
        ))
        return engine.connect()
