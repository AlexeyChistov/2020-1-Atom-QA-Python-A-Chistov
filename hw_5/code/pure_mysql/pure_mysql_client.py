import pymysql
from pymysql.cursors import DictCursor
from sqlalchemy.orm import sessionmaker

from config import Config
from pure_mysql.pure_mysql_builder import PureMysqlBuilder


class PureMysqlConnection(object):
    def __init__(self):
        config: Config = Config()
        self.user = config.USER
        self.password = config.PASSWORD
        self.db_name = config.PURE_SQL_DB_NAME
        self.table_name = config.PURE_SQL_TABLE_NAME
        self.port = config.PORT
        self.host = config.HOST
        self.connection = self.connect()
        session = sessionmaker(bind=self.connection)
        self.session = session()
        self.builder: PureMysqlBuilder = PureMysqlBuilder(self.table_name)

    def connect(self):
        connection = self.get_connection()
        connection.query(f'DROP DATABASE IF EXISTS {self.db_name}')
        connection.query(f'CREATE DATABASE IF NOT EXISTS {self.db_name}')
        connection.close()
        return self.get_connection(is_db_created=True)

    def get_connection(self, is_db_created=False):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db_name if is_db_created else None,
            cursorclass=DictCursor,
            autocommit=True,
            charset='utf8'
        )

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def init_tables(self):
        self.execute_query(self.builder.create_logs_table())
