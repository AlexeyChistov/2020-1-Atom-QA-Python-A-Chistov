import sqlalchemy
from sqlalchemy.orm import sessionmaker
from config import Config


class MysqlOrmConnection(object):
    def __init__(self):
        config: Config = Config()
        self.user = config.USER
        self.password = config.PASSWORD
        self.db_name = config.PURE_SQL_DB_NAME
        self.port = config.PORT
        self.host = config.HOST
        self.connection = self.connect()
        session = sessionmaker(bind=self.connection)
        self.session = session()

    def get_connection(self, db_created=False):
        engine = sqlalchemy.create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            db=self.db_name if db_created else ''
        ))
        return engine.connect()

    def connect(self):
        connection = self.get_connection(db_created=False)
        connection.execute(f'DROP DATABASE IF EXISTS {self.db_name}')
        connection.execute(f'CREATE DATABASE {self.db_name}')
        connection.close()
        return self.get_connection(db_created=True)
