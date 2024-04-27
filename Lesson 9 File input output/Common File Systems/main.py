import csv
import os
import boto3
import botocore
from azure.storage.blob import BlobServiceClient
from google.cloud import storage

# Function to read CSV file
def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Read CSV file from Linux or Windows
def read_local_csv(file_path):
    if os.name == 'posix':  # Linux
        read_csv(file_path)
    elif os.name == 'nt':   # Windows
        read_csv(file_path.replace('/', '\\'))

# Read CSV file from AWS S3
def read_s3_csv(bucket_name, file_name):
    s3 = boto3.client('s3')
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        data = response['Body'].read().decode('utf-8')
        print(data)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "NoSuchKey":
            print("The object does not exist.")
        else:
            raise

# Read CSV file from Azure Blob Storage
def read_blob_csv(connection_string, container_name, blob_name):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    data = blob_client.download_blob().readall().decode('utf-8')
    print(data)

# Read CSV file from Google Cloud Storage
def read_gcs_csv(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    data = blob.download_as_text()
    print(data)

# Example usage:
if __name__ == "__main__":
    # Local file path (Linux/Windows)
    read_local_csv('/path/to/sample.csv')

    # AWS S3
    read_s3_csv('bucket_name', 'sample.csv')

    # Azure Blob Storage
    read_blob_csv('YOUR_CONNECTION_STRING', 'container_name', 'sample.csv')

    # Google Cloud Storage
    read_gcs_csv('bucket_name', 'sample.csv')
