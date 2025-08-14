# Medallion Architecture – ETL Pipeline for Brazilian CEP Data

This project implements an ETL (Extract, Transform, Load) pipeline focused on Brazilian CEP (postal code) data. The pipeline extracts data from a public API, performs normalization and transformation, and stores the results as Parquet files locally or on AWS S3.

## Technologies Used

| Technology      | Description                                       |
| :--------------- | :------------------------------------------------- |
| **Python 3.8+** | Programming language used for ETL scripts.        |
| **Requests**    | Python library to fetch data from the public API. |
| **Pandas**      | Data manipulation and transformation.             |
| **PyArrow**     | For handling Parquet files efficiently.           |
| **Boto3**       | AWS SDK for uploading files to S3.                |
| **AWS S3**      | Cloud storage for raw and processed data.         |


	


## Project Structure
```
├── 01-bronze-raw/             Storage for raw data (Bronze)
├── 02-silver-validated/       Cleaned/validated data (Silver)
├── normalize_data.py          Script for data normalization and transformation
├── script.py                  Main pipeline execution script
└── upload_to_s3.py            Script to upload Parquet files to AWS S3
```

* **01-bronze-raw/:** stores the raw extracted data.
* **02-silver-validated/:** stores cleaned and transformed data.
* **normalize_data.py:** applies transformations, type conversions, and cleaning.
* **script.py:** orchestrates the full ETL pipeline.
* **upload_to_s3.py:** uploads Parquet files to an S3 bucket.

## Requirements

* Python 3.8+
* requests
* boto3
* pandas
* pyarrow
* AWS credentials configured with write permissions for S3.

## Usage
1. Install dependecies

2. Run the full pipeline: **python script.py**

3. Upload processed files to S3: **python upload_to_s3.py**

## Architecture Diagram
graph TD
    API[API CEP] --> Bronze[Bronze (Raw Data)]
    Bronze --> Silver[Silver (Cleaned / ETL)]
