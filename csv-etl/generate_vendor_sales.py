import pandas as pd
import random
from datetime import datetime, timedelta

countries = ["US", "USA", "United States", "U.S."]
data = []

for i in range(2000):
    order_date = datetime(2026, 1, 1) + timedelta(days=random.randint(0, 60))
    date_formats = [
        order_date.strftime("%d-%m-%Y"),
        order_date.strftime("%Y/%m/%d"),
        order_date.strftime("%Y-%m-%d")
    ]
    data.append([
        i,
        random.randint(100, 200),
        random.choice(date_formats),
        random.choice([random.randint(100, 1000), None]),
        random.choice(countries)
    ])

df = pd.DataFrame(data, columns=["order_id","customer_id","order_date","amount","country"])

# Add duplicates
df = pd.concat([df, df.sample(100)])

df.to_csv("vendor_sales.csv", index=False)
print("Generated 2100 records with duplicates.")
