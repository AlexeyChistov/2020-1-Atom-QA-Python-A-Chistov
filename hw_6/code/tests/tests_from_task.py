from conftest import Base


class Test(Base):
    def test_create_user(self):
        username = "user1"
        self.app_socket_requests.post(
            'create/user',
            data={"username": f"{username}"},
            header={"username": f"{username}"}
        )
        assert self.user_client._check_user(username) != (False, None)

    def test_create_post(self):
        username = "user1"
        post_title = "post1"
        self.app_socket_requests.post(
            'create/user',
            data={"username": f"{username}"},
            header={"username": f"{username}"}
        )
        user_id = self.user_client._check_user(username)[1]
        self.app_socket_requests.put(
            'create/post',
            data={"username": f"{username}", "post_title": f"{post_title}"},
            header={"username": f"{username}", "post_title": f"{post_title}"}
        )
        assert self.user_client._check_posts(user_id, post_title) is True

    def test_user_already_exists(self):
        username = "user2"
        response_1 = self.app_socket_requests.post(
            'create/user',
            data={"username": f"{username}"},
            header={"username": f"{username}"}
        )
        response_2 = self.app_socket_requests.post(
            'create/user',
            data={"username": f"{username}"},
            header={"username": f"{username}"}
        )
        assert response_1 == "New user added", 200
        assert response_2 == "User already exist", 200

    def test_post_already_exists(self):
        username = "user2"
        post_title = "post1"
        self.app_socket_requests.post(
            'create/user',
            data={"username": f"{username}"},
            header={"username": f"{username}"}
        )
        response_1 = self.app_socket_requests.put(
            'create/post',
            data={"username": f"{username}", "post_title": f"{post_title}"},
            header={"username": f"{username}", "post_title": f"{post_title}"}
        )
        response_2 = self.app_socket_requests.put(
            'create/post',
            data={"username": f"{username}", "post_title": f"{post_title}"},
            header={"username": f"{username}", "post_title": f"{post_title}"}
        )
        assert response_1 == "New post added", 200
        assert response_2 == "Post already exists", 200


    def test_mock_500(self):
        assert self.app_socket_requests.get('/500') == "Error status code 500"

    def test_no_headers(self):
        username = "user4"
        response = self.app_socket_requests.post(
            'create/user',
            data={"username": f"{username}"}
        )
        assert response == "Header error", 412

    def test_headers_data(self):
        username = "user5"
        response = self.app_socket_requests.post(
            'create/user',
            data={"username": f"{username}"},
            header={"use": f"{username}+qwerty"}
        )
        assert response == "Header error", 412

    def test_mock_is_down(self, init_http_mock):
        init_http_mock.stop()
        assert init_http_mock.server_run is False
