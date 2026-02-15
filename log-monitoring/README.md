# Log Monitoring Project

## Objective
Process application logs and generate monitoring insights.

## Setup

1. Create virtual environment:
   python -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install pandas

3. Folder structure
log-monitoring/
│── data/
│    └── app_logs.json
│── src/
│    └── process_logs.py
│── README.md

## Tasks
- Parse JSON logs
- Calculate:
  - Error rate per hour
  - Top failing endpoints
  - Average response time
- Generate output reports in CSV format

## Deliverables
- process_logs.py
- summary_report.csv
- error_summary.json

## Evaluation
- Modular code
- Error handling
- Performance considerations
