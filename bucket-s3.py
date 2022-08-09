#Create bucket

import boto3   

bucket = boto3.resource('s3')
response = bucket.create_bucket(
    Bucket = 'boto3_create_bucket',
    ACL = "private" #public-read/public-read-write/private

    # CreateBucketConfiguration = {
    #     'LocationConstraint':'us-east-1' #default, don't need put this block
    # }
)

print(response)

#=======================================
#Create bucket with Client

import boto3 

client = boto3.client('s3')
response = client.create_bucket(
    Bucket = 'BucketName',
    ACL = 'private',

    CreateBucketConfiguration = {
        'LocationConstraint': 'sa-east-1'
    }
)
print (response)
#========================================
#Uploading Image to Bucket S3

import boto3 

client = boto3.client('s3')

with open('aws.png','rb')as f:
    data = f.read()

response = client.put_object(
    ACL = "private", #public-read/public-read-write/private
    Bucket = "Bucket_Name",
    Body = data,
    Key = "aws.png"

)

print(response)
#=========================================
#Listing All Buckets

import boto3 

bucket = boto3.client('s3')
response = bucket.list_buckets()

print("Listing All Buckets")

for bucket in response ['Buckets']:
    print(bucket['Name'])

#Other Way
resource = boto3.resource('s3') 
iterator = resource.buckets.all()
print("Listing all buckets")

for bucket in iterator:
    print(bucket)


#===========================
#Delete Bucket S3

import boto3 
 
client = boto3.client('s3')
bucket_name = "name_bucket"

client.delete_bucket(Bucket=bucket_name)

print("S3 Bucket has been deleted")

#otherway

resource = boto3.resource('s3')
bucket_name = "Bucket_Name"

s3_bucket = resource.Bucket(bucket_name)
s3_bucket.delete()

print("This {} has been deleted ".format(s3_bucket))

#==============================
#Delete Not Empty Bucket

import boto3 

BUCKET_NAME = "Bucket_Name"
s3_resource = boto3.resource('s3')

s3_bucket = s3_resource.Bucket(BUCKET_NAME)

def clean_up():
    #Delete the object
    for s3_object in s3_bucket.objects.all():
        s3_object.delete()

    #Delete bucket versioning 

    for s3_object_ver in s3_bucket.object_version.all():
        s3_object_ver.delete()

    print("S3 bucket cleaned")

clean_up()

s3_bucket.delete()

print("Bucket has been deleted")
#=====================================
#Upload File 

import boto3 

bucket_name = "bucket_name"

s3_client = boto3.client('s3')

def upload_files(file_name,bucket,object_name=None):
    if object_name is None:
        object_name = file_name
    s3_client.upload_file(file_name,bucket,object_name,ExtraArgs=args)
    print("{} has been uploaded to {}".format(file_name,bucket_name))

upload_files("file.txt",bucket_name)

#Otherway uploading with resource

bucket_name = "bucket_name"

s3_client = boto3.resource('s3')

def upload_files(file_name,bucket,object_name=None):
    if object_name is None:
        object_name = file_name

    s3_client.meta.client.upload_file(file_name,bucket,object_name,ExtraArgs=args)
    print("{} has been uploaded to {}".format(file_name,bucket_name))

upload_files("file.pdf",bucket_name)

#========================
#Download File

import boto3 

bucket_name = "Bucket_Name"

s3_resource = boto3.resource('s3')
s3_object = s3_resource.Object(bucket_name,'file.pdf')
s3_object.download_file('downloaded.pdf')

print("File has been downloaded")
#====================================
#Listing Files

import boto3 

bucket_name = "Bucket_Name"

s3_resource = boto3.resource('s3')
s3_bucket = s3_resource.Bucket(bucket_name)

print("Listing Bucket Files or Objects")

for obj in s3_bucket.objects.all():
    print(obj.key)

#========================================
#Listing filter objects

import boto3 

bucket_name = "Bucket_Name"

s3_resource = boto3.resource('s3')
s3_bucket = s3_resource.Bucket(bucket_name)

print("Listing Filtered File")

for obj in s3_bucket.objects.filter(Prefix="file"):
    print(obj.key)

#======================================
#Get Summary of Object

import boto3 

s3 = boto3.resource('s3')
object_summary = s3.ObjectSummary("Bucket_Name","file.pdf")

print(object_summary.bucket_name)
print(object_summary.key)

#===================================
#Copy an Object to another bucket

import boto3 

s3 = boto3.resource('s3')

copy_source = {
    'Bucket':'Bucket_Name1',
    'Key':'file.pdf'
}

s3.meta.client.copy(copy_source,'bucket_name2', 'copied.pdf')

#====================================
#Delete an object 

import boto3 

client = boto3.client('s3')
response = client.delete_object(
    Bucket = 'Bucket_Name',
    Key = 'file.pdf'
)

print(response)

#delete multiple files or objects

response = client.delete_objects(
    Bucket = 'Bucket_Name',
    Delete = {
        'Objects':[
            {
                'Key':'file.pdf'
            },
            {
                'Key':'otherfile.pdf'
            }

        ]
    }
)
print(response)
#=====================================
#Delete attached policy from bucket

import boto3 

client = boto3.client('s3')

response = client.delete_bucket_policy(
    bucket = "Bucket_Name"
)
print (response)
