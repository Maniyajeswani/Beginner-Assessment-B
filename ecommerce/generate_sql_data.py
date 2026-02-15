import random
from datetime import datetime, timedelta

customers = 1000
products = 200
orders = 5000

print("-- Customers")
for i in range(1, customers+1):
    print(f"INSERT INTO customers VALUES ({i}, 'Customer{i}', "
          f"'{random.choice(['North','South','East','West'])}', "
          f"'2025-01-{random.randint(1,28)}');")

print("\n-- Products")
for i in range(1, products+1):
    print(f"INSERT INTO products VALUES ({i}, 'Product{i}', "
          f"'{random.choice(['Electronics','Clothing','Home'])}', "
          f"{random.randint(10,2000)});")

print("\n-- Orders")
for i in range(1, orders+1):
    date = datetime(2026,1,1) + timedelta(days=random.randint(0,60))
    print(f"INSERT INTO orders VALUES ({i}, "
          f"{random.randint(1,customers)}, "
          f"'{date.date()}', "
          f"{random.randint(1,products)}, "
          f"{random.randint(1,5)});")
