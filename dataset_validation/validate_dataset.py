import pandas as pd
import os

# get current folder path
BASE_DIR = os.path.dirname(__file__)

# load datasets
customers = pd.read_csv(os.path.join(BASE_DIR, "olist_customers_dataset.csv"))
orders = pd.read_csv(os.path.join(BASE_DIR, "olist_orders_dataset.csv"))
payments = pd.read_csv(os.path.join(BASE_DIR, "olist_order_payments_dataset.csv"))


def validate_missing_customer():
    # check orders with invalid customer
    invalid = orders[~orders["customer_id"].isin(customers["customer_id"])]
    print(f"Orders with invalid customer: {len(invalid)}")


def validate_missing_orders():
    # check payments with invalid order
    invalid = payments[~payments["order_id"].isin(orders["order_id"])]
    print(f"Payments with invalid order: {len(invalid)}")


def validate_payment_values():
    # check payment values <= 0
    invalid = payments[payments["payment_value"] <= 0]
    print(f"Invalid payment values: {len(invalid)}")


def validate_duplicate_orders():
    # check duplicate orders
    duplicates = orders[orders.duplicated("order_id")]
    print(f"Duplicate orders: {len(duplicates)}")


def validate_empty_fields():
    # check null values
    null_orders = orders["order_id"].isnull().sum()
    null_customers = customers["customer_id"].isnull().sum()

    print(f"Null order IDs: {null_orders}")
    print(f"Null customer IDs: {null_customers}")


def validate_order_status():
    # check missing order status
    missing = orders["order_status"].isnull().sum()
    print(f"Orders with missing status: {missing}")


def validate_delivery_dates():
    # convert to datetime
    orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
    orders["order_delivered_customer_date"] = pd.to_datetime(
        orders["order_delivered_customer_date"], errors="coerce"
    )

    # check delivery before purchase
    invalid = orders[
        orders["order_delivered_customer_date"] < orders["order_purchase_timestamp"]
    ]

    print(f"Invalid delivery timelines: {len(invalid)}")


def validate_payment_per_order():
    # check too many payments per order
    count = payments.groupby("order_id").size()
    abnormal = count[count > 3]

    print(f"Orders with too many payments: {len(abnormal)}")


def main():
    print("Running dataset validation\n")

    validate_missing_customer()
    validate_missing_orders()
    validate_payment_values()
    validate_duplicate_orders()
    validate_empty_fields()

    print("\nAdvanced checks\n")

    validate_order_status()
    validate_delivery_dates()
    validate_payment_per_order()

    print("\nDone")


if __name__ == "__main__":
    main()