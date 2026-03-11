import os
os.environ["HADOOP_HOME"] = "C:\\tmp"

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = (
    SparkSession.builder
    .appName("SalesTransformation")
    .master("local[*]")
    .config("spark.hadoop.io.native.lib.available", "false")
    .config("spark.sql.sources.commitProtocolClass",
            "org.apache.spark.sql.execution.datasources.SQLHadoopMapReduceCommitProtocol")
    .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "2")
    .getOrCreate()
)

# Load data
customers = spark.read.csv("data/customers.csv", header=True, inferSchema=True)
products = spark.read.csv("data/products.csv", header=True, inferSchema=True)
orders = spark.read.json("data/api_orders.json")

# Join tables
sales = orders.join(customers, "customer_id") \
              .join(products, "product_id")

# Calculate revenue
sales = sales.withColumn(
    "revenue",
    col("quantity") * col("price")
)

# Select analytics columns
analytics = sales.select(
    "order_id",
    "customer_id",
    "name",
    "product_name",
    "category",
    "quantity",
    "price",
    "revenue",
    "order_date"
)

# Save analytics dataset
analytics.coalesce(1) \
    .write \
    .mode("overwrite") \
    .option("header", True) \
    .option("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false") \
    .csv("data/analytics_sales")

print("Analytics dataset created.")

spark.stop()