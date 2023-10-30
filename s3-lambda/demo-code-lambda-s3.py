import boto3

def lambda_handler(event, context):
    Account = "jerrybean"
    RawBucketName1 = "input-bucket"
    RawBucketName2 = "output-bucket"
    Region = "us-east-2"

    source_bucket_name = "-".join([Account,Region,RawBucketName1]) # Replace with your source bucket name
    destination_bucket_name = "-".join([Account,Region,RawBucketName2])  # Replace with your destination bucket name

    s3 = boto3.client('s3')

    # List objects in the source bucket
    response = s3.list_objects_v2(Bucket=source_bucket_name)

    for obj in response.get('Contents', []):
        # Copy each object to the destination bucket
        s3.copy_object(CopySource={'Bucket': source_bucket_name, 'Key': obj['Key']}, Bucket=destination_bucket_name, Key=obj['Key'])

    return {
        'statusCode': 200,
        'body': 'Objects copied from source bucket to destination bucket'
    }
