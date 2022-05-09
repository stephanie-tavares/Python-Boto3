import boto3

aws_console=boto3.session.Session(profile_name="your-profile")
iam_resource=aws_console.resource(service_name="iam",region_name="us-east-1")

for each_item in iam_resource.users.all():
	print(each_item.user_name)
