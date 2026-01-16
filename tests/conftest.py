import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "http://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def session():
    return requests.Session()
