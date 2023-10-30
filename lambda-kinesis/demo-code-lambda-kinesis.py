import json
import boto3
import base64

s3 = boto3.client('s3')
kinesis = boto3.client('kinesis')

def lambda_handler(event, context):
    for record in event['Records']:
        # Decode the base64-encoded data from the Kinesis record
        #record = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        encoded_data = record['kinesis']['data']
        decoded_data = json.loads(encoded_data.decode("utf-8"))
        save_to_s3(decoded_data)
        
def save_to_s3(data):
    bucket_name = 'jerrybean-us-east-2-output-bucket'
    object_key = 'TestKinesis/'+str(data['timestamp'])+'.json'
    jsondata = json.dumps(data)
    # Upload the data to S3
    s3.put_object(Bucket=bucket_name, Key=object_key, Body=jsondata)

    print(f"Data saved to S3: {bucket_name}/{object_key}")
