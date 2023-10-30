import boto3

kinesis = boto3.client('kinesis')

def read_records_from_kinesis(stream_name, shard_id):
    response = kinesis.get_shard_iterator(
        StreamName=stream_name,
        ShardId=shard_id,
        ShardIteratorType='LATEST'  # Use 'TRIM_HORIZON' for reading from the beginning
    )
    shard_iterator = response['ShardIterator']

    while True:
        response = kinesis.get_records(
            ShardIterator=shard_iterator,
            Limit=10  # You can adjust the number of records to retrieve
        )

        for record in response['Records']:
            data = record['Data']
            print(f"Received data: {data}")

        shard_iterator = response['NextShardIterator']

stream_name = 'your-stream-name'
shard_id = 'your-shard-id'

read_records_from_kinesis(stream_name, shard_id)

