import pandas as pd
import random
import json
from datetime import datetime, timedelta

# Orders JSON
orders = []
start = datetime(2026,1,1)

for i in range(8000):
    orders.append({
        "order_id": i,
        "customer_id": random.randint(1,1000),
        "product_id": random.randint(1,300),
        "quantity": random.randint(1,5),
        "order_date": (start + timedelta(days=random.randint(0,60))).strftime("%Y-%m-%d")
    })

with open("api_orders.json","w") as f:
    json.dump(orders, f)

print("Generated full end-to-end dataset.")
