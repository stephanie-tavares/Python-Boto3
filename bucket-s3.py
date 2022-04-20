import boto3
from boto3 import Session #Take the AWS profile without needed pass in plan text

boto_sess = Session(profile_name = 'your-profile-name',region_name='your-region')

client = boto3.client('s3')
client.create_bucket(Bucket = 'Bucket name')
print('Success')
