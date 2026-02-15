# PySpark Batch ETL

## Objective
Process daily transaction dataset using PySpark.

## Setup
1. Install Spark
2. Start Spark session
3. Load CSV from data folder

## Tasks
- Remove failed transactions
- Deduplicate records
- Partition output by transaction_date
- Write parquet output

## Deliverables
- etl_job.py
- Output parquet files
