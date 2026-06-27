
import os
import io
import boto3
import pandas as pd


AWS_ENDPOINT = os.getenv("AWS_ENDPOINT_URL")
BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

AWS_ACCESS_KEY = "test"
AWS_SECRET_KEY = "test"


def create_client():
    return boto3.client(
        "s3",
        endpoint_url=AWS_ENDPOINT,
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
        region_name="us-east-1",
    )


def read_csv_from_s3(client):
    print("Reading input file...")

    response = client.get_object(
        Bucket=BUCKET_NAME,
        Key="raw/input.csv"
    )

    dataframe = pd.read_csv(
        io.BytesIO(response["Body"].read())
    )

    return dataframe


def transform_data(df):
    print("Transforming data...")

    df["double_value"] = df["value"] * 2

    df = df[df["value"] >= 100]

    return df


def upload_to_s3(client, df):
    print("Uploading transformed file...")

    csv_buffer = io.StringIO()

    df.to_csv(csv_buffer, index=False)

    client.put_object(
        Bucket=BUCKET_NAME,
        Key="processed/output.csv",
        Body=csv_buffer.getvalue()
    )


def main():
    client = create_client()

    df = read_csv_from_s3(client)

    transformed_df = transform_data(df)

    upload_to_s3(client, transformed_df)

    print("ETL Pipeline Completed Successfully")


if __name__ == "__main__":
    main()