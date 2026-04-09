import requests
from config import GRAPHQL

def test_country_query():
    # GraphQL query
    query = {
        "query": """
        {
          country(code: "IE") {
            name
            capital
          }
        }
        """
    }

    response = requests.post(GRAPHQL, json=query)

    assert response.status_code == 200

    data = response.json()

    # validate response
    assert data["data"]["country"]["name"] == "Ireland"