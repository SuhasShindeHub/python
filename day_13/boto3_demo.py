import boto3

client = boto3.client('s3')


response = client.delete_bucket(
    Bucket='suhas-boto3-demo-2025',
)

print(response)

response = client.delete_bucket(
    Bucket='suhas-boto3-demo-25',
)



print(response)