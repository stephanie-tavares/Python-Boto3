#import já declarado nas primeiras linhas, obrigatorio
import boto3
import pprint 

#Mostra na tela a descrição de uma EC2
ec2_client = boto3.client('ec2')
response = ec2_client.describe_instances() 
pprint (response)

#====================

#Criando par de chave 

resp = ec2_client.create_key_pair(
    KeyName = 'minha-chave',
    KeyType = 'rsa'
)

#pprint (resp['KeyMaterial'])

#guardando o arquivo pem 
file = open('minha-chave.pem','w')
file.write(resp[ 'KeyMaterial'])
file.close() 

#=====================
#SecurityGroup

#import boto3 
#import pprint 

ec2_client = boto3.client('ec2')
response = ec2_client.create_security_group(
    Description = "This is desc",
    GroupName = "PyGroup",
    VpcId = "id-vpc",
)

pprint (response)

#===================
#Criando regras de entrada

ec2_client = boto3.client('ec2')

response = ec2_client.authorize_security_group_ingress(
    GroudId = 'group-id',
    IpPermission =[
        {
        'IpProtocol':'tcp',
        'FromPort':80,
        'ToPort':80,
        'IpRanges':[{'CidrIp':'0.0.0.0/0','Description':'Descrição'}]
        },
        {
        'IpProtocol':'tcp',
        'FromPort':22,
        'ToPort':22,
        'IpRanges':[{'CidrIp':'0.0.0.0/0','Description':'Descrição'}]
        }
    ]
)
pprint(response)

#===============================
#Criando EC2

ec2_resource = boto3.resource('ec2')

response = ec2_resource.create_instance(
    ImageId = 'ami-xxxx',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'minha-chave',
    SecurityGroups = [
        'pygroup'
    ]
)
pprint (response)

#==================================
#Pegando IP publico 

def get_ip(instance_id):
    ec2_client = boto3.client('ec2')
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get('Reservations')

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get('PublicIpAddress'))

get_ip('instance-id')

#===================================
#Listando EC2 ativa

def get_instances():
    ec2_client = boto3.client('ec2')

    reservations = ec2_client.describe_instances().get('Reservations')

    for reservation in reservations:
        for instance in reservation[ 'Instances']:
            instance_id = instance[ 'InstanceId']
            instance_type = instance[ 'InstanceType']
            public_ip = instance['PublicIpAddress']
            private_ip = instance[ 'PrivateIpAddress']
            
            print(f'{instance_id}, {instance_type}, {public_ip}, {private_ip}')

#=====================================
#Para EC2

def stop_instance(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.stop_instances(InstanceIds=[instance_id])

    print (response)

stop_instance('id-xxxx')

#======================================
#Excluir EC2 (Terminate)

def terminate_instance(Instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.terminate_instances(InstanceIds=[Instance_id])

    print (response)

terminate_instance('id-xxxx')

#========================================
#Descrevendo EC2 Secuirty Group

ec2_client = boto3.client('ec2')

response = ec2_client.describe_security_groups()
pprint(response)

#===================================
#Deletar SecurityGroup 

ec2_client = boto3.client('ec2')

response = ec2_client.delete_security_group(
    GroupId = 'id-xxx'
)

print(response)

#===================================
#Deletar par de chaves 

ec2_client = boto3.client('ec2')
response = ec2_client.delete_key_pair(
    KeyName = 'minha-chave'
)

print (response)

#==================================
#Usando filtro na descrição da EC2

ec2_client = boto3.client('ec2')
reservations = ec2_client.describe_instances(Filters=[
    {
        "Name":"instance-state-name",
        "Values":["runing","stopped"]
    }
]).get("Reservations")

for reservation in reservations: 
    for instance in reservation["Instances"]:
        instance_id = instance["InstanceId"]
        instance_type = instance["InstanceType"]
        
#====================================
