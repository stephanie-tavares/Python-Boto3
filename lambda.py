#Example:

from inspect import Attribute
import json
from msilib import Table 

def lambda_handler(event,context):
    return{
        'statusCode':200,
        'body': json.dumps('Hello from Lambda!')
    }

#==================================
#Listing S3 buckets using lambda
#Needed the access role

import json 
import boto3 

s3 = boto3.resource('s3')
def lambda_handler(event,context):
    s3_buckets=[]

    for bucket in s3.buckets.all():
        s3_buckets.append(bucket.name)
    
    return {
        "statusCode": 200,
        "body": s3_buckets
    }

#=================================
#Upload image

import boto3 

def lambda_handler(event,context):
    client = boto3.client('s3')

    with open('aws.png','rb') as f: 
        data=f.read()

        response = client.put_object(
            Bucket = "bucketname",
            Body = data,
            Key = 'aws.png'
            )

#========================================
#Create dynamoDB Tables

import boto3 

def lambda_handler(event,context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName = 'Users',
        KeySchema = [ 
            {
                'AtrtributeName':'id',
                'KeyType':'HASH'
            }
        ],

        AttributeDefinitions = [
            {
                'AtrtributeName':'id',
                'KeyType':'N'               
            }
        ],

        ProvisionedThroughput = {
            'ReadCapacityUnits':3,
            'WriteCapacityUnits':3 
        }

    )

print ("Table status: ", Table.table_status)