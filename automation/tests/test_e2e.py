from clients.reqres_client import create_user
from utils.retry import retry
import requests
from config import ORDERS

def test_e2e_flow():
    # create user
    user_payload = {
        "name": "charan",
        "job": "qa"
    }

    user_res = retry(lambda: create_user(user_payload))
    assert user_res.status_code == 201

    user_id = user_res.json().get("id")

    # create order
    order_payload = {
        "userId": int(user_id) if user_id else 1,
        "title": "order",
        "body": "test order"
    }

    order_res = retry(lambda: requests.post(f"{ORDERS}/posts", json=order_payload))
    assert order_res.status_code in [200, 201]

    # validate relationship
    assert order_res.json()["userId"] == int(user_id)