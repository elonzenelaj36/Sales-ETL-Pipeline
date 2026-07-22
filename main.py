from pathlib import Path

from logger import logger

from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.validator import validate_data
from pipeline.save_processed import save_processed_data
from pipeline.save_rejected import save_rejected_data
from pipeline.generate_report import generate_report
from pipeline.load import load_data


def main():

    logger.info("Starting ETL pipeline...")
    print("Starting ETL pipeline...")

    BASE_DIR = Path(__file__).resolve().parent
    file = BASE_DIR / "data" / "raw" / "sales.csv"


    # Extract
    print("Extracting data...")
    data = extract_data(file)


    # Transform
    print("Transforming data...")
    cleaned_data = transform_data(data)


    # Validate
    print("Validating data...")
    validated_data, rejected_data = validate_data(cleaned_data)


    # Save processed data
    print("Saving processed data...")
    save_processed_data(validated_data)


    # Save rejected data
    print("Saving rejected data...")
    save_rejected_data(rejected_data)


    # Load into database
    print("Loading data...")
    load_data(validated_data)


    # Generate report
    print("Generating report...")
    generate_report(
        data,
        validated_data,
        rejected_data
    )


    logger.info("ETL pipeline finished successfully!")
    print("ETL pipeline finished successfully!")


if __name__ == "__main__":
    main()