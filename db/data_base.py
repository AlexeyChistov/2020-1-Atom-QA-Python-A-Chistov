import pymysql
from pymysql.cursors import DictCursor


class MysqlConnection(object):
    def __init__(self, user, password, db_name, mock=False):
        self.user = user
        self.password = password
        self.db_name = db_name
        # if mock:
        #     self.host = '192.168.1.10'
        # else:
        self.host = 'db'
        self.port = 3306
        self.charset = 'utf8'
        self.connection = self.connect()

    # todo: db_create = False по сути мне это не нужно, тк я создаю дб при компоузе
    def get_connection(self, db_created=False):
        return pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db_name if db_created else None,
            charset=self.charset,
            cursorclass=DictCursor,
            autocommit=True
        )

    def connect(self):
        connection = self.get_connection(db_created=False)
        connection.close()
        return self.get_connection(db_created=True)

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
