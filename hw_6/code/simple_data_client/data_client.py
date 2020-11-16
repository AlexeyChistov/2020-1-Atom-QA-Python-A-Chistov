import json

"""Зарегистрированные пользовтели id: [username]"""
USERS_DATA = {}

"""Посты пользователей id: [post1, post2 ...]"""
POSTS_DATA = {}


class UserClient:
    """
    Добваление пользователя,
    создание постов.
    """
    def __init__(self):
        self._users_data = USERS_DATA
        self._posts_data = POSTS_DATA
        self._id_counter = len(self._users_data)

    def _check_posts(self, user_id, post_title, post_exists=False):
        if len(self._posts_data[user_id]) == 0:
            return False
        else:
            for posts in self._posts_data[user_id]:
                if post_title != posts:
                    post_exists = False
                else:
                    post_exists = True
        return post_exists

    def _check_user(self, new_user, user_exists=True):
        for user_id in self._users_data.keys():
            if new_user != self._users_data[user_id][0]:
                user_exists = False
            else:
                user_exists = True
                return user_exists, user_id
        return False, None

    def registration(self, new_user):
        user_exists, user_id = self._check_user(new_user)
        if not user_exists:
            self._id_counter += 1
            self._users_data[self._id_counter] = [f"{new_user}"]
            self._posts_data[self._id_counter] = []
            return "User added"
        return "User already exists"

    def idempotent_create_post(self, user_name, post_title):
        try:
            user_exists, user_id = self._check_user(user_name)
        except KeyError:
            user_exists = False
            user_id = None
        if user_exists:
            post_exists = self._check_posts(user_id, post_title)
            if not post_exists:
                self._posts_data[user_id].append(post_title)
                return "New post created"
            else:
                return "Post already exists"
        else:
            return "User doesnt exists"

    def show_data(self):
        data = {}
        for user_id in self._users_data.keys():
            data[self._users_data[user_id][0]] = []
            for post in self._posts_data[user_id]:
                data[self._users_data[user_id][0]].append(post)
        return json.dumps(data, sort_keys=True, indent=4)
