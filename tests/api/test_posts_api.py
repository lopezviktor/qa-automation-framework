import pytest


@pytest.mark.parametrize("post_id", [1, 2, 3, 10])
def test_get_post_by_id_returns_expected_id(session, base_url, post_id):
    response = session.get(f"{base_url}/posts/{post_id}")

    assert response.status_code == 200

    post = response.json()
    assert isinstance(post, dict)

    assert "id" in post
    assert isinstance(post["id"], int)
    assert post["id"] == post_id


def test_get_posts_returns_200(session, base_url):
    response = session.get(f"{base_url}/posts")
    assert response.status_code == 200


def test_get_posts_returns_list(session, base_url):
    response = session.get(f"{base_url}/posts")
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_single_post_has_expected_fields(session, base_url):
    response = session.get(f"{base_url}/posts/1")
    post = response.json()

    expected_fields = ["userId", "id", "title", "body"]

    for field in expected_fields:
        assert field in post

    assert isinstance(post["userId"], int)
    assert isinstance(post["id"], int)
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)


def test_get_nonexistent_post_returns_404(session, base_url):
    response = session.get(f"{base_url}/posts/999999")
    assert response.status_code == 404

    # JSONPlaceholder typically returns an empty JSON object for missing resources.
    # Keep the assertion tolerant in case the body is empty.
    body_text = response.text.strip()
    assert body_text in ("", "{}")
