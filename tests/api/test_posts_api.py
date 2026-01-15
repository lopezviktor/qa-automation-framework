import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts_returns_200():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200


def test_get_posts_returns_list():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_single_post_has_expected_fields():
    response = requests.get(f"{BASE_URL}/posts/1")
    post = response.json()

    expected_fields = ["userId", "id", "title", "body"]

    for field in expected_fields:
        assert field in post

    assert isinstance(post["userId"], int)
    assert isinstance(post["id"], int)
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)
