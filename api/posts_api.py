from api.base_client import BaseClient

class PostsAPI(BaseClient):
    ENDPOINT = "/posts"

    def get_all_posts(self, params=None):
        return self.get(self.ENDPOINT, params=params)

    def get_post_by_id(self, post_id):
        return self.get(f"{self.ENDPOINT}/{post_id}")

    def create_post(self, title, body, userId):
        return self.post(self.ENDPOINT, payload={
            "title": title, "body": body, "userId": userId
        })

    def update_post(self, post_id, title, body, userId):
        return self.put(f"{self.ENDPOINT}/{post_id}", payload={
            "id": post_id, "title": title, "body": body, "userId": userId
        })

    def partial_update_post(self, post_id, **kwargs):
        return self.patch(f"{self.ENDPOINT}/{post_id}", payload=kwargs)

    def delete_post(self, post_id):
        return self.delete(f"{self.ENDPOINT}/{post_id}")