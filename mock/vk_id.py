import threading
from flask import Flask, jsonify

from db.data_base import MysqlConnection


class Mock:
    app = Flask(__name__)

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run_app(self):
        server = threading.Thread(target=self.app.run, kwargs={
            "host": self.host,
            "port": self.port
        })
        server.start()
        server.join(1)

        return server

    @staticmethod
    @app.errorhandler(404)
    def err(e):
        return jsonify({"Error": "bad request"}), 404

    @staticmethod
    @app.route('/', methods=['GET'])
    def index():
        return {"server status": "ok"}, 200

    @staticmethod
    @app.route('/vk_id/<username>', methods=['GET'])
    def get_id(username):
        """Реализация в соответствии с ТЗ"""
        # todo: В отдельный файл все конфигаруционные данные 'test_qa', 'qa_test', 'technoatom'
        mysql: MysqlConnection = MysqlConnection('root', 'pass', 'technoatom', mock=True)
        try:
            sql_response = mysql.execute_query(f"SELECT id FROM test_users WHERE username = '{username}';")[0]
            return jsonify(sql_response), 200
        except:
            return jsonify({}), 404

    @staticmethod
    @app.route('/check/<username>', methods=['GET'])
    def get_table_data(username):
        """
        Получаем все данные пользователя из таблицы (по <username>), если он присутствует, статускод 200:
        {"username":<username>, "email":<email>,"id":<id>,"password":<password> ...}
        В противном случае получаем {} и статускод 404
        """
        mysql: MysqlConnection = MysqlConnection('root', 'pass', 'technoatom', mock=True)
        try:
            sql_response = mysql.execute_query(f"SELECT * FROM test_users WHERE username = '{username}';")[0]
            return jsonify(sql_response), 200
        except:
            return jsonify({}), 404


if __name__ == '__main__':
    a = Mock('0.0.0.0', 1122)
    a.run_app()
