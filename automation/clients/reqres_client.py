import requests
from config import REQRES, API_KEY

HEADERS = {
    "x-api-key": API_KEY
}

def create_user(payload):
    # create user API
    return requests.post(f"{REQRES}/users", json=payload, headers=HEADERS)

def get_users():
    # fetch users
    return requests.get(f"{REQRES}/users?page=2", headers=HEADERS)