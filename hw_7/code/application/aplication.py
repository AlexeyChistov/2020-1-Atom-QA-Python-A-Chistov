from application import config
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    users = config.USERS_DATA
    if username in users and check_password_hash(users.get(username), password):
        return username


@app.route('/')
@auth.login_required
def index():
    return f'Hello, {auth.current_user()}!'


@app.route('/profile')
@auth.login_required
def profile():
    return f'{auth.current_user()}, this is your profile!'


@app.route('/album')
@auth.login_required
def album():
    return "Album!"


@app.route('/photos')
@auth.login_required
def photos():
    return "Photos!"


@app.route('/shareware')
def shareware():
    return "Free for all!"


@app.route('/logout')
@auth.login_required
def logout():
    return f'{auth.current_user()} was logout!', 401


if __name__ == "__main__":
    app.run(debug=False, host=config.APP_CONFIG["host"], port=config.APP_CONFIG["port"])
