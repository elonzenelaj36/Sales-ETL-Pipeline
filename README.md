# Sales Data Pipeline

An ETL (Extract, Transform, Load) data pipeline built with Python and MySQL.

The project reads raw sales data from CSV files, cleans and validates the data, stores processed records in a MySQL database, and generates business reports.

---

## Project Overview

This pipeline simulates a real-world data engineering workflow:

1. Extract data from CSV files
2. Transform and clean raw data
3. Validate data quality
4. Separate rejected records
5. Save processed data
6. Load clean data into MySQL database
7. Generate sales reports
8. Track pipeline execution using logs

---

## Technologies Used

- Python 3
- Pandas
- SQLAlchemy
- MySQL
- PyMySQL
- python-dotenv
- Logging module

---

## Project Structure

sales-data-pipeline/

│
├── data/
│ ├── raw/
│ │ └── sales.csv
│ │
│ ├── processed/
│ │ └── clean_sales.csv
│ │
│ └── rejected/
│ └── rejected_sales.csv
│
├── database/
│ ├── connection.py
│ └── schema.sql
│
├── pipeline/
│ ├── extract.py
│ ├── transform.py
│ ├── validator.py
│ ├── save_processed.py
│ ├── save_rejected.py
│ ├── load.py
│ └── generate_report.py
│
├── logs/
│ └── pipeline.log
│
├── reports/
│ └── sales_report.txt
│
├── main.py
├── requirements.txt
└── README.md

---

# ETL Pipeline Flow

Raw CSV
|
v
Extract
|
v
Transform
|
v
Validate
|
+------------+
| |
Valid Data Rejected Data
| |
v v
Processed CSV Rejected CSV
|
v
MySQL Database
|
v
Reports


---

# Data Transformation

The transformation step performs:

- Cleaning customer names
- Standardizing date formats
- Removing missing dates
- Removing duplicate orders
- Creating total sales column

Example:

Before:
customer = " sara "
date = "2026/07/17"

After:
customer = "Sara"
date = "2026-07-17"


---

# Data Validation

The validation stage checks:

- Quantity must be greater than 0
- Price must be greater than 0
- Order ID cannot be empty
- Order date cannot be missing

Invalid records are stored separately:data/rejected/rejected_sales.csv


---

# Database

The pipeline loads cleaned data into MySQL.

Example table:
sales

order_id
order_date
customer
product
quantity
price
total
created_at


---

# Logging

Pipeline execution is monitored using logs.

Example:
2026-07-18 17:41:14 | INFO |
Starting ETL pipeline...

Extracted 10 rows

Rows after transformation: 6

Rows after validation: 6

Loaded 6 rows into database

ETL pipeline finished successfully!


Log file:logs/pipeline.log


---

# Reports

The pipeline generates a business report containing:

- Total input rows
- Processed rows
- Rejected rows
- Total revenue
- Top product
- Top customer
- Pipeline status

Example:
ETL SALES REPORT

Input rows:
11

Processed rows:
6

Rejected rows:
1

Total Revenue:
$3780

Top Product:
Mouse

Top Customer:
Elon

Pipeline Status:
SUCCESS


---

# Installation

Clone the repository:

bash
git clone <repository-url>

Create virtual environment:
python -m venv venv

Activate environment:

Linux:
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt




Database Setup

Create MySQL database:
CREATE DATABASE sales_db;

Run schema:

mysql -u username -p sales_db < database/schema.sql

Configure database connection in:
database/connection.py




Running the Pipeline

Run:
python main.py

Expected output:

Starting ETL pipeline...
Extracting data...
Transforming data...
Validating data...
Saving processed data...
Loading data...
Data loaded successfully!

ETL pipeline finished successfully!


