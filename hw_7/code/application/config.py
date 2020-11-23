from werkzeug.security import generate_password_hash


APP_CONFIG = {
    "host": "0.0.0.0",
    "port": 2021
}

USERS_DATA = {
    "user_1": generate_password_hash("111"),
    "user_2": generate_password_hash("222")
}
