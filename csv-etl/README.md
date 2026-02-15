# CSV ETL Cleaning Project

## Objective
Clean messy vendor data before warehouse loading.

## Tasks
- Remove duplicates
- Standardize date format (YYYY-MM-DD)
- Normalize country column
- Fill missing amounts with 0
- Output cleaned_sales.csv

## Folder Structure
csv-etl/
│── data/
│    └── vendor_sales.csv

## Bonus
- Add CLI argument for input/output file paths

## Expected Output
cleaned_sales.csv
etl_log.txt
