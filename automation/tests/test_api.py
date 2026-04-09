import pytest
from clients.reqres_client import create_user, get_users

@pytest.mark.parametrize("name", ["charan", "test_user"])
def test_create_user(name):
    # data-driven test
    payload = {
        "name": wername,
        "job": "qa"
    }

    response = create_user(payload)

    assert response.status_code == 201
    assert response.json()["name"] == name


def test_get_users():
    response = get_users()

    assert response.status_code == 200
    assert len(response.json()["data"]) > 0