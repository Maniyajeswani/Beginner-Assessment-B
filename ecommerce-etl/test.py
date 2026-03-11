import sqlite3

conn = sqlite3.connect("warehouse/ecommerce.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM customers LIMIT 5")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()