import boto3
import os
from datetime import datetime

# Replace this with your actual bucket name from AWS
BUCKET_NAME = "vante-automation-logs"

# Create an S3 client
s3 = boto3.client("s3")

# Define the folder and file types to upload
folder_path = os.getcwd()  # current directory
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

print("🪣 Uploading .log files to S3...")

# Upload each .log file
for file_name in os.listdir(folder_path):
    if file_name.endswith(".log"):
        file_path = os.path.join(folder_path, file_name)
        s3_key = f"logs/{timestamp}_{file_name}"
        s3.upload_file(file_path, BUCKET_NAME, s3_key)
        print(f"✅ Uploaded {file_name} → s3://{BUCKET_NAME}/{s3_key}")

print("🚀 All log files uploaded successfully!")
