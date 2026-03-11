import pandas as pd
import random
from datetime import datetime, timedelta

N = 50000
regions = ["North","South","East","West","Central"]

data = []
start = datetime(2024,1,1)

for i in range(1, N+1):
    signup = start + timedelta(days=random.randint(0, 700))
    data.append([
        i,
        f"Customer{i}",
        random.choice(regions),
        signup.strftime("%Y-%m-%d"),
        True,
        signup.strftime("%Y-%m-%d"),
        None
    ])

df = pd.DataFrame(data, columns=[
    "customer_id","name","region",
    "signup_date","is_current",
    "effective_from","effective_to"
])

# Add SCD Type 2 changes (10% customers move region)
updates = df.sample(int(N*0.1))

scd_records = []
for _, row_series in updates.iterrows():
    change_date = datetime(2026,1,1)

    # Create the 'old' SCD record (the one that becomes non-current)
    old_record_values = row_series.tolist()
    # Modify the values in the list directly
    old_record_values[4] = False # 'is_current' column
    old_record_values[6] = change_date.strftime("%Y-%m-%d") # 'effective_to' column
    scd_records.append(old_record_values)

    # Create the 'new' SCD record
    scd_records.append([
        row_series["customer_id"],
        row_series["name"],
        random.choice(regions),
        row_series["signup_date"],
        True,
        change_date.strftime("%Y-%m-%d"),
        None
    ])

df = pd.concat([df, pd.DataFrame(scd_records, columns=df.columns)])
df.to_csv("ecommerce-etl\data\customers.csv", index=False)

print("Generated 50K customers + SCD records.")