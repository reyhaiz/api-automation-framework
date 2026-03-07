import pytest
from utils.assertions import Assertions

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "username", "email"],
    "properties": {
        "id":       {"type": "integer"},
        "name":     {"type": "string"},
        "username": {"type": "string"},
        "email":    {"type": "string"}
    }
}

class TestGetUsers:

    @pytest.mark.positive
    @pytest.mark.smoke
    def test_get_all_users_status_200(self, users_api):
        r = users_api.get_all_users()
        Assertions.assert_status_code(r, 200)

    @pytest.mark.positive
    def test_get_all_users_returns_10(self, users_api):
        r = users_api.get_all_users()
        Assertions.assert_list_length(r.json(), 10)

    @pytest.mark.positive
    def test_get_user_by_id_valid_schema(self, users_api, existing_user_id):
        r = users_api.get_user_by_id(existing_user_id)
        Assertions.assert_json_schema(r.json(), USER_SCHEMA)

    @pytest.mark.positive
    def test_get_user_posts_not_empty(self, users_api, existing_user_id):
        r = users_api.get_user_posts(existing_user_id)
        Assertions.assert_list_not_empty(r.json())

    @pytest.mark.negative
    def test_get_nonexistent_user_404(self, users_api):
        r = users_api.get_user_by_id(99999)
        Assertions.assert_status_code(r, 404)

    @pytest.mark.boundary
    def test_get_first_user_id_1(self, users_api):
        r = users_api.get_user_by_id(1)
        Assertions.assert_status_code(r, 200)

    @pytest.mark.boundary
    def test_get_last_user_id_10(self, users_api):
        r = users_api.get_user_by_id(10)
        Assertions.assert_status_code(r, 200)