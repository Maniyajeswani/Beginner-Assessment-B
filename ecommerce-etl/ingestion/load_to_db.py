import pandas as pd
import sqlite3
import json
import os

import os

DB_PATH = "../warehouse/ecommerce.db"

# create folder if not exists
os.makedirs("../warehouse", exist_ok=True)

conn = sqlite3.connect(DB_PATH)
# Data folder
DATA_PATH = "data"
def load_customers(conn):
    print("Loading customers...")

    df = pd.read_csv(os.path.join(DATA_PATH, "customers.csv"))

    df.to_sql(
        "customers",
        conn,
        if_exists="append",
        index=False
    )

    print(f"Inserted {len(df)} customers")


def load_products(conn):
    print("Loading products...")

    df = pd.read_csv(os.path.join(DATA_PATH, "products.csv"))

    df.to_sql(
        "products",
        conn,
        if_exists="append",
        index=False
    )

    print(f"Inserted {len(df)} products")


def load_orders(conn):
    print("Loading orders...")

    with open(os.path.join(DATA_PATH, "api_orders.json")) as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    df.to_sql(
        "orders",
        conn,
        if_exists="append",
        index=False
    )

    print(f"Inserted {len(df)} orders")


def main():

    print("Connecting to database...")

    conn = sqlite3.connect(DB_PATH)

    load_customers(conn)
    load_products(conn)
    load_orders(conn)

    conn.commit()
    conn.close()

    print("Data successfully loaded!")


if __name__ == "__main__":
    main()