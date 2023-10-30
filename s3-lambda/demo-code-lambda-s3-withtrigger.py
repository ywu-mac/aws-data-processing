import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Retrieve the source bucket and key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_key = event['Records'][0]['s3']['object']['key']

    # Destination bucket where you want to write data
    destination_bucket = 'jerrybean-us-east-2-output-bucket'

    try:

        s3.copy_object(CopySource={'Bucket': source_bucket, 'Key': source_key}, Bucket=destination_bucket_name, Key=source_key)

        return {
            'statusCode': 200,
            'body': 'Success'
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        raise e
