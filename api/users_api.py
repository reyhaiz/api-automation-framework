from api.base_client import BaseClient

class UsersAPI(BaseClient):
    ENDPOINT = "/users"

    def get_all_users(self):
        return self.get(self.ENDPOINT)

    def get_user_by_id(self, user_id):
        return self.get(f"{self.ENDPOINT}/{user_id}")

    def get_user_posts(self, user_id):
        return self.get(f"{self.ENDPOINT}/{user_id}/posts")