from pathlib import Path

from logger import logger


def generate_report(raw_df, clean_df, rejected_df):

    BASE_DIR = Path(__file__).resolve().parent.parent

    report_file = BASE_DIR / "reports" / "sales_report.txt"

    total_sales = clean_df["total"].sum()

    top_product = (
        clean_df.groupby("product")["total"]
        .sum()
        .idxmax()
    )

    top_customer = (
        clean_df.groupby("customer")["total"]
        .sum()
        .idxmax()
    )


    report = f"""
ETL SALES REPORT
================

Input rows:
{len(raw_df)}

Processed rows:
{len(clean_df)}

Rejected rows:
{len(rejected_df)}


Total Revenue:
${total_sales}


Top Product:
{top_product}


Top Customer:
{top_customer}


Pipeline Status:
SUCCESS
"""


    with open(report_file, "w") as file:
        file.write(report)


    logger.info(f"Report generated: {report_file}")