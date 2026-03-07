import pytest
from utils.assertions import Assertions
from utils.data_generator import DataGenerator

POST_SCHEMA = {
    "type": "object",
    "required": ["userId", "id", "title", "body"],
    "properties": {
        "userId": {"type": "integer"},
        "id":     {"type": "integer"},
        "title":  {"type": "string"},
        "body":   {"type": "string"}
    }
}

# ─────────────────────────────────────────────
# POSITIVE TESTS
# ─────────────────────────────────────────────
class TestGetPosts:

    @pytest.mark.positive
    @pytest.mark.smoke
    def test_get_all_posts_status_200(self, posts_api):
        """GET /posts → harus 200"""
        r = posts_api.get_all_posts()
        Assertions.assert_status_code(r, 200)

    @pytest.mark.positive
    def test_get_all_posts_returns_100_items(self, posts_api):
        """GET /posts → harus kembalikan 100 post"""
        r = posts_api.get_all_posts()
        Assertions.assert_list_length(r.json(), 100)

    @pytest.mark.positive
    def test_get_all_posts_response_time(self, posts_api):
        """GET /posts → harus respons < 2 detik"""
        r = posts_api.get_all_posts()
        Assertions.assert_response_time(r, 2000)

    @pytest.mark.positive
    def test_get_all_posts_content_type_json(self, posts_api):
        """GET /posts → Content-Type harus application/json"""
        r = posts_api.get_all_posts()
        Assertions.assert_content_type(r, "application/json")

    @pytest.mark.positive
    @pytest.mark.smoke
    def test_get_post_by_id_status_200(self, posts_api, existing_post_id):
        """GET /posts/1 → harus 200"""
        r = posts_api.get_post_by_id(existing_post_id)
        Assertions.assert_status_code(r, 200)

    @pytest.mark.positive
    def test_get_post_by_id_correct_schema(self, posts_api, existing_post_id):
        """GET /posts/1 → schema harus sesuai"""
        r = posts_api.get_post_by_id(existing_post_id)
        Assertions.assert_json_schema(r.json(), POST_SCHEMA)

    @pytest.mark.positive
    def test_get_post_by_id_correct_value(self, posts_api, existing_post_id):
        """GET /posts/1 → 'id' di response harus 1"""
        r = posts_api.get_post_by_id(existing_post_id)
        Assertions.assert_field_value(r.json(), "id", existing_post_id)

    @pytest.mark.positive
    def test_filter_posts_by_userid(self, posts_api):
        """GET /posts?userId=1 → semua item harus userId=1"""
        r = posts_api.get_all_posts(params={"userId": 1})
        data = r.json()
        Assertions.assert_list_not_empty(data)
        for post in data:
            assert post["userId"] == 1


class TestCreatePost:

    @pytest.mark.positive
    @pytest.mark.smoke
    def test_create_post_status_201(self, posts_api):
        """POST /posts → harus 201 Created"""
        r = posts_api.create_post(**DataGenerator.valid_post())
        Assertions.assert_status_code(r, 201)

    @pytest.mark.positive
    def test_create_post_returns_id(self, posts_api):
        """POST /posts → response harus punya 'id'"""
        r = posts_api.create_post(**DataGenerator.valid_post())
        Assertions.assert_field_exists(r.json(), "id")

    @pytest.mark.positive
    def test_create_post_title_matches(self, posts_api):
        """POST /posts → 'title' di response = yang dikirim"""
        payload = DataGenerator.valid_post()
        r = posts_api.create_post(**payload)
        Assertions.assert_field_value(r.json(), "title", payload["title"])


class TestUpdatePost:

    @pytest.mark.positive
    def test_put_post_status_200(self, posts_api, existing_post_id):
        """PUT /posts/1 → harus 200"""
        r = posts_api.update_post(existing_post_id, "New Title", "New body", 1)
        Assertions.assert_status_code(r, 200)

    @pytest.mark.positive
    def test_patch_post_title_updated(self, posts_api, existing_post_id):
        """PATCH /posts/1 → 'title' harus berubah"""
        new_title = "Patched Title"
        r = posts_api.partial_update_post(existing_post_id, title=new_title)
        Assertions.assert_field_value(r.json(), "title", new_title)


class TestDeletePost:

    @pytest.mark.positive
    def test_delete_post_status_200(self, posts_api, existing_post_id):
        """DELETE /posts/1 → harus 200"""
        r = posts_api.delete_post(existing_post_id)
        Assertions.assert_status_code(r, 200)

    @pytest.mark.positive
    def test_delete_post_empty_response(self, posts_api, existing_post_id):
        """DELETE /posts/1 → body response harus {}"""
        r = posts_api.delete_post(existing_post_id)
        assert r.json() == {}


# ─────────────────────────────────────────────
# NEGATIVE TESTS
# ─────────────────────────────────────────────
class TestNegativePosts:

    @pytest.mark.negative
    def test_get_nonexistent_post_404(self, posts_api, nonexistent_post_id):
        """GET /posts/99999 → harus 404"""
        r = posts_api.get_post_by_id(nonexistent_post_id)
        Assertions.assert_status_code(r, 404)

    @pytest.mark.negative
    def test_get_post_string_id_404(self, posts_api):
        """GET /posts/abc → ID string tidak valid, harus 404"""
        r = posts_api.get_post_by_id("abc")
        Assertions.assert_status_code(r, 404)

    @pytest.mark.negative
    def test_get_post_negative_id_404(self, posts_api):
        """GET /posts/-1 → ID negatif tidak valid, harus 404"""
        r = posts_api.get_post_by_id(-1)
        Assertions.assert_status_code(r, 404)


# ─────────────────────────────────────────────
# BOUNDARY TESTS
# ─────────────────────────────────────────────
class TestBoundaryPosts:

    @pytest.mark.boundary
    def test_get_first_post_id_1(self, posts_api):
        """GET /posts/1 → ID minimum harus berhasil"""
        r = posts_api.get_post_by_id(1)
        Assertions.assert_status_code(r, 200)

    @pytest.mark.boundary
    def test_get_last_post_id_100(self, posts_api):
        """GET /posts/100 → ID maksimum harus berhasil"""
        r = posts_api.get_post_by_id(100)
        Assertions.assert_status_code(r, 200)

    @pytest.mark.boundary
    def test_get_post_id_101_not_found(self, posts_api):
        """GET /posts/101 → satu lebih dari max, harus 404"""
        r = posts_api.get_post_by_id(101)
        Assertions.assert_status_code(r, 404)

    @pytest.mark.boundary
    def test_create_post_empty_title(self, posts_api):
        """POST /posts dengan title kosong → 201 atau 400"""
        r = posts_api.create_post(**DataGenerator.post_empty_title())
        assert r.status_code in [201, 400]

    @pytest.mark.boundary
    def test_create_post_very_long_title(self, posts_api):
        """POST /posts dengan title 10.000 karakter → 201/400/413"""
        r = posts_api.create_post(**DataGenerator.post_very_long_title(10000))
        assert r.status_code in [201, 400, 413]