import json

from locust import HttpUser, task, between, TaskSet


class User1Scenario(TaskSet):
    user_data = {"user": "user_1", "pass": 111}

    def on_start(self):
        r = self.client.get('/', auth=(self.user_data["user"], self.user_data["pass"]))
        self.client.headers.update({'Authorization': r.request.headers['Authorization']})
        assert 200 == r.status_code

    def on_stop(self):
        r = self.client.get('/logout')
        assert r.status_code == 401

    @task
    def profile(self):
        r = self.client.get("/profile")
        assert r.text == f'{self.user_data["user"]}, this is your profile!'

    @task
    def profile_album(self):
        r_1 = self.client.get('/profile')
        assert r_1.text == f'{self.user_data["user"]}, this is your profile!'
        r_2 = self.client.get('/album')
        assert r_2.text == "Album!"

    @task
    def album_photos(self):
        r_1 = self.client.get('/album')
        assert r_1.text == "Album!"
        r_2 = self.client.get('/photos')
        assert r_2.text == "Photos!"


class User2Scenario(TaskSet):
    user_data = {"user": "user_2", "pass": 222}

    def on_start(self):
        r = self.client.get('/', auth=(self.user_data["user"], self.user_data["pass"]))
        self.client.headers.update({'Authorization': r.request.headers['Authorization']})
        assert 200 == r.status_code

    def on_stop(self):
        r = self.client.get('/logout')
        assert r.status_code == 401

    @task
    def shareware(self):
        r = self.client.get('/shareware')
        assert r.text == "Free for all!"
        assert r.status_code == 200

    @task
    def photos(self):
        r = self.client.get('/photos')
        assert "Photos!" == r.text
        assert r.status_code == 200

    @task
    def profile(self):
        r = self.client.get("/profile")
        assert r.text == f'{self.user_data["user"]}, this is your profile!'
        assert r.status_code == 200


class WebSiteUser(HttpUser):
    tasks = [User1Scenario, User2Scenario]
    wait_time = between(1, 2)
