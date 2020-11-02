from log_maker.log_maker import LogMaker


class PureMysqlBuilder(LogMaker):
    def __init__(self, table_name):
        self.table_name = table_name
        self.create_logs_table()
        self.log = self.fake_logger()
        self.insert_log()

    def create_logs_table(self):
        return f"""
        CREATE TABLE IF NOT EXISTS `{self.table_name}` (
        `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
        `ip` VARCHAR(30) NOT NULL ,
        `date` VARCHAR(20) NOT NULL ,
        `method` VARCHAR(10) NOT NULL ,
        `url` VARCHAR(255) NOT NULL ,
        `resp_code` INT NOT NULL
        ) CHARSET=utf8
        """

    def insert_log(self):
        log = self.log
        return f"""
        INSERT INTO {self.table_name} VALUE (
        NULL,
        '{log['ip']}',
        '{log['date']}',
        '{log['method']}',
        '{log['url']}',
        '{log['resp_code']}'
        )
        """

    def show_table_record(self):
        return f"SELECT * FROM {self.table_name}"
