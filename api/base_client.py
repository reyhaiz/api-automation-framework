import requests
from config.config import Config

class BaseClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.timeout  = Config.TIMEOUT
        self.session  = requests.Session()
        self.session.headers.update(Config.HEADERS)

    def get(self, endpoint, params=None):
        return self.session.get(f"{self.base_url}{endpoint}",
                                params=params, timeout=self.timeout)

    def post(self, endpoint, payload=None):
        return self.session.post(f"{self.base_url}{endpoint}",
                                 json=payload, timeout=self.timeout)

    def put(self, endpoint, payload=None):
        return self.session.put(f"{self.base_url}{endpoint}",
                                json=payload, timeout=self.timeout)

    def patch(self, endpoint, payload=None):
        return self.session.patch(f"{self.base_url}{endpoint}",
                                  json=payload, timeout=self.timeout)

    def delete(self, endpoint):
        return self.session.delete(f"{self.base_url}{endpoint}",
                                   timeout=self.timeout)