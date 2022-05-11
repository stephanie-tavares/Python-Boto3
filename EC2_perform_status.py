#===============================EC2 management using Python/Boto3===============================================================##
from pickle import TRUE
import boto3
import sys 

PROFILE_NAME = "your-profile"
REGION = "us-east-1"
SERVICE_NAME = "ec2"
IMAGE_ID = "ami-1111111"
INSTANCE_TYPE="t2.micro"
SUBNET_ID="subnet-222222222"


aws_management_console=boto3.session.Session(profile_name=PROFILE_NAME)
ec2_console_resource=aws_management_console.resource(service_name=SERVICE_NAME,region_name=REGION)

while TRUE:
    print("This script performs the following actions on ec2 instance: ")
    print("""
        1. New
        2. start
        3. stop
        4. terminate
        5. exit
        """)

    option=int(input("Enter your option: "))
    if option ==1:
        instances = ec2_console_resource.create_instances(
        ImageId=IMAGE_ID,
        MinCount=1,
        MaxCount=1,
        InstanceType=INSTANCE_TYPE,
        SubnetId=SUBNET_ID,
    )
        print("Instance ID: ",instances)
        sys.exit()

    elif option ==2:
        instance_id=input("Enter your EC2 instance Id: ")
        my_req_instance_object=ec2_console_resource.Instance(instance_id)
        print(dir(my_req_instance_object))
        print("Starting EC2 instance...")
        my_req_instance_object.start()

    elif option ==3:
        instance_id=input("Enter your EC2 instance Id: ")
        my_req_instance_object=ec2_console_resource.Instance(instance_id)
        print("Stopping EC2 instance...")
        my_req_instance_object.stop()
    
    elif option ==4:
        instance_id=input("Enter your EC2 instance Id: ")
        my_req_instance_object=ec2_console_resource.Instance(instance_id)
        print("Terminating EC2 instance...")
        my_req_instance_object.terminate()

    elif option ==5:
        print("Thanks for using this script!")
        sys.exit()

    else:
        print("Your option is invalid, please try once again...")
