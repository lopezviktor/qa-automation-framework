import pytest

from jsonschema import validate
from tests.schemas.post_schema import POST_SCHEMA


@pytest.mark.regression
@pytest.mark.parametrize("post_id", [1, 2, 3, 10])
def test_get_post_by_id_returns_expected_id(session, base_url, post_id):
    response = session.get(f"{base_url}/posts/{post_id}", timeout=5)

    assert response.status_code == 200

    post = response.json()
    validate(instance=post, schema=POST_SCHEMA)

    assert isinstance(post, dict)

    assert "id" in post
    assert isinstance(post["id"], int)
    assert post["id"] == post_id


@pytest.mark.smoke
def test_get_posts_returns_200(session, base_url):
    response = session.get(f"{base_url}/posts", timeout=5)
    assert response.status_code == 200


@pytest.mark.smoke
def test_get_posts_returns_list(session, base_url):
    response = session.get(f"{base_url}/posts", timeout=5)
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


@pytest.mark.regression
def test_single_post_has_expected_fields(session, base_url):
    response = session.get(f"{base_url}/posts/1", timeout=5)
    post = response.json()

    expected_fields = ["userId", "id", "title", "body"]

    for field in expected_fields:
        assert field in post

    assert isinstance(post["userId"], int)
    assert isinstance(post["id"], int)
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)


@pytest.mark.regression
def test_get_nonexistent_post_returns_404(session, base_url):
    response = session.get(f"{base_url}/posts/999999", timeout=5)
    assert response.status_code == 404

    # JSONPlaceholder typically returns an empty JSON object for missing resources.
    # Keep the assertion tolerant in case the body is empty.
    body_text = response.text.strip()
    assert body_text in ("", "{}")


@pytest.mark.contract
def test_single_post_matches_schema(session, base_url):
    response = session.get(f"{base_url}/posts/1", timeout=5)
    assert response.status_code == 200

    post = response.json()
    validate(instance=post, schema=POST_SCHEMA)


@pytest.mark.contract
def test_posts_list_matches_schema(session, base_url):
    response = session.get(f"{base_url}/posts", timeout=5)
    assert response.status_code == 200

    posts = response.json()
    assert isinstance(posts, list)

    for post in posts:
        validate(instance=post, schema=POST_SCHEMA)


@pytest.mark.security
def test_posts_response_has_json_content_type(session, base_url):
    response = session.get(f"{base_url}/posts", timeout=5)
    assert response.status_code == 200

    content_type = response.headers.get("Content-Type")
    assert content_type is not None
    assert content_type.startswith("application/json")


@pytest.mark.security
def test_error_response_do_not_leak_stack_traces(session, base_url):
    response = session.get(f"{base_url}/posts/999999", timeout=5)

    body = response.text.lower()

    forbidden_markers = [
        "traceback",
        "exception",
        "stack trace",
        "nullpointer",
        "sql",
        "/usr/",
        "at ",
    ]
    for marker in forbidden_markers:
        assert marker not in body
