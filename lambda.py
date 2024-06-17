import boto3
import os

s3 = boto3.client('s3')

def lambda_handler(event, context):
    source_path = '/tmp/'  # Use /tmp in Lambda
    bucket_name = ''  # Replace with your S3 bucket name
    key_prefix = ''  # S3 key prefix (folder path)

    for root, dirs, files in os.walk(source_path):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_file_key = key_prefix + file

            try:
                s3.upload_file(local_file_path, bucket_name, s3_file_key)
                print(f"Uploaded {local_file_path} to s3://{bucket_name}/{s3_file_key}")
            except Exception as e:
                print(f"Failed to upload {local_file_path} to S3: {str(e)}")

    return {
        'statusCode': 200,
        'body': 'File upload successful!'
    }
