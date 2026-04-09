import json

def load_data():
    # load test data from json file
    with open("test_data.json") as f:
        return json.load(f)


def check_user_order(data):
    # collect all valid user ids
    user_ids = [user["id"] for user in data["users"]]

    # verify each order has a valid user reference
    for order in data["orders"]:
        if order["userId"] not in user_ids:
            print(f"Invalid userId {order['userId']} in order {order['id']}")


def check_payment(data):
    # map order id to its amount
    order_map = {order["id"]: order["amount"] for order in data["orders"]}

    for payment in data["payments"]:
        order_id = payment["orderId"]

        # check if payment refers to an existing order
        if order_id not in order_map:
            print(f"Payment for missing order {order_id}")

        # check if payment matches order amount
        elif payment["paid"] != order_map[order_id]:
            print(f"Payment mismatch for order {order_id}")


def main():
    # run all validations
    data = load_data()
    check_user_order(data)
    check_payment(data)


if __name__ == "__main__":
    main()