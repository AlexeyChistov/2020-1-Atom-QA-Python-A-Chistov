from sqlalchemy.engine import Connection
from orm_mysql.models.orm_model import Model, Base


class OrmSqlBuilder(object):
    def __init__(self, connection: Connection, session, table_name):
        self.connection = connection
        self.engine = self.connection.engine
        self.session = session
        self.table_name = table_name

    def create_log_table(self):
        if not self.engine.dialect.has_table(self.engine, self.table_name):
            Base.metadata.tables[self.table_name].create(self.engine)

    def insert_log(self, log: Model):
        self.session.add(log)
        self.session.commit()

    def show_log(self):
        return self.session.query(Model).all()
