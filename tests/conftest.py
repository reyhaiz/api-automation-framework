import pytest
from api.posts_api import PostsAPI
from api.users_api import UsersAPI

@pytest.fixture(scope="session")
def posts_api():
    return PostsAPI()

@pytest.fixture(scope="session")
def users_api():
    return UsersAPI()

@pytest.fixture(scope="session")
def existing_post_id():
    return 1

@pytest.fixture(scope="session")
def nonexistent_post_id():
    return 99999

@pytest.fixture(scope="session")
def existing_user_id():
    return 1