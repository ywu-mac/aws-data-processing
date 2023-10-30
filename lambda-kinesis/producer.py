import boto3
import json
import random
import time
import base64

aws_region = 'us-east-2'
stream_name = 'jerrybean-us-east-2-test-stream-2'

kinesis = boto3.client('kinesis', region_name=aws_region)

def put_record_to_kinesis(stream_name, data, partition_key):

    #data_to_send = bytes(json.dumps(data).encode("utf-8"))
    print(type(data))
    json_data = json.dumps(data)
    print(json_data)
    print(type(json_data))
    encoded_data = json_data.encode("utf-8")
    print(encoded_data)
    print(type(encoded_data))
    print(bytes(json.dumps(data).encode("utf-8"))==encoded_data)
    b64e = base64.b64encode(encoded_data)
    print(b64e)
    print(type(b64e))
    data_to_send = b64e.decode("utf-8")
    print(data_to_send)
    print(type(data_to_send))
    print(base64.b64decode(b64e))
    print(base64.b64decode(data_to_send))

    #dictionary to json string to binary data to b64 encoded bytes and again to ASCII string, both b64 encoded bytes and ASCII string can be decoded.
    #Decode back to 


    # response = kinesis.put_record(
    #     StreamName=stream_name,
    #     Data=data_to_send,
    #     PartitionKey=partition_key
    # )
    # return response

#while True:
for i in range(1):
    data = {
        'sensor_id': random.randint(1, 10),
        'temperature': round(random.uniform(20.0, 30.0), 2),
        'timestamp': int(time.time())
    }
    put_record_to_kinesis(stream_name, data, str(data['sensor_id']))

    # response = put_record_to_kinesis(stream_name, data, str(data['sensor_id']))
    # print(f"Record sent: ShardId={response['ShardId']} SequenceNumber={response['SequenceNumber']}")
    
    # Sleep for a few seconds before sending the next record
    time.sleep(1)

