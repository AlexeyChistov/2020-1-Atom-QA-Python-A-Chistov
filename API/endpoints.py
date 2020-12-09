from urllib.parse import urljoin


class RoutesForApi:
    base_url = "http://myapp:8081/"

    def auth_user_url(self):
        url = urljoin(self.base_url, "/login")
        return url

    def app_status_url(self):
        url = urljoin(self.base_url, "/status")
        return url

    def add_user_url(self):
        url = urljoin(self.base_url, "/api/add_user")
        return url

    def del_user_url(self, username):
        url = urljoin(self.base_url, f"/api/del_user/{username}")
        return url

    def block_user_url(self, username):
        url = urljoin(self.base_url, f"/api/block_user/{username}")
        return url

    def accept_user_url(self, username):
        url = urljoin(self.base_url, f"/api/accept_user/{username}")
        return url

    @staticmethod
    def user_info(username):
        """Роут на мок, для спаршивания табличных данных некоторого пользователя"""
        return f"http://vk_id/check/{username}"
