import boto3

aws_console=boto3.session.Session(profile_name="profile-name")
ec2=aws_console.client(service_name="ec2",region_name="us-east-1")

response=ec2.describe_instances()['Reservations']
for each_item in response:
	for each in each_item['Instances']:
		print("=============================")
		print("The Image Id is: {}\nThe Instance Id Is: {}\nThe Instance Launch Time is: {}".format(each['ImageId'],each['InstanceId'],each['LaunchTime'].strftime("%Y-%m-%d")))

response=ec2.describe_volumes()['Volumes']
for each_item in response:
	print("=======================")
	print("The volume id is: {}\nThe AvailabilityZone is: {}\nThe VolumeType is: {}".format(each_item['VolumeId'],each_item['AvailabilityZone'],each_item['VolumeType']))
