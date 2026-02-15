# End-to-End E-Commerce Data Platform

## Objective
Simulate a mini production-grade data platform.

## Flow
1. Python ingestion from API JSON
2. Store raw data in SQL
3. PySpark transformations
4. Build analytics layer
5. Write SQL KPI queries

## Project structure
ecommerce-platform/
│── ingestion/
│── warehouse/
│── spark_jobs/
│── data/
│    ├── api_orders.json
│    ├── customers.csv
│    └── products.csv

## Requirements
- Modular code
- Logging
- Config-driven design
- Clear documentation

## Deliverables
- ingestion scripts
- SQL DDL + DML
- Spark transformation job
- Analytical queries
- Architecture diagram (optional)
