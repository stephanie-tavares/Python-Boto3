'''List existing buckets'''

import boto3
from boto3 import Session

boto_sess = Session(profile_name = 'your-profile',region_name='your region')

client = boto3.client('s3')
response = client.list_buckets()
print(response)
