from xml.etree.ElementTree import tostring
import boto3 
#Inserindo dados em uma tabela no DynamoDB

db = boto3.resource('dynamodb')

table = db.Table('employee')

table.put_item(
    Item = {
        'emp_id':"2",
        'name':"test",
        'age':24
    }
)

#====================================
#inserindo dados
import boto3 

db =  boto3.client('dynamodb')
response = db.put_item(
    TableName = 'employee',
    Item = {
        'emp_id':{
            'S':'3'
        },
        'name':{
            'S':'newname'
        },
        'age':{
            'S':30
        }
    }
)

#=======================================
#BathWrite 
import boto3 

db = boto3.resource('dynamodb')
table = db.Table('employee')

with table.batch_writer() as batch:
    batch.put_item(
        Item = {
            'emp_id':'5',
            'name':'outronome',
            'age':'35'
        }
    )

    batch.put_item(
        Item = {
            'emp_id':'6', 
            'name': 'outronome2',
            'age': '20'
        }
    )
    
    batch.put_item(
        Item = {
            'emp_id':'7', 
            'name': 'outronome3',
            'age': '40'
        }
    )

#=================================
#Descrever uma tabela DynamoDB
import boto3
import pprint

db = boto3.client('dynamodb')

response = db.describe_table(
    TableName = 'table_name'
)

pprint(response)

#=====================================
#Listando tabelas do dynamoDB 
import boto3 
import pprint 

db = boto3.client('dynamodb')
response = db.list_tables()

pprint(response)

#===============================
#update dynamodb
import boto3 

db = boto3.client('dynamodb')

response = db.update_table(
    TableName = 'table_name',
    BillingMode = 'Provisioned',
    ProvisionedThroughput = {
        'ReadCapacityunits': 5,
        'WriteCapacityUnits': 5
    }
)

#=================================
#Criando backup

import boto3 

db = boto3.client('dynamodb')

response = db.create_backup(
    TableName='table_name',
    BackupName='TableBackup'
)

print (response)

#deletando o backup 
response = db.delete_backup(
    BackupArn = ''

)
print (response)

#====================================
#Pegando um item do DynamoDB

import boto3 

db = boto3.resource('dynamodb')

table = db.Table('table_name')

response = table.get_item(
    Key = {
        'emp_id':"1"
    }
)

print (response['Item'])

#================================
#BatchGetItem

import boto3 
import pprint 

db = boto3.resource('dynamodb')

response = db.batch_get_item(
    RequestItem = {
        'table_name': {
            'Keys': [
                {
                    'emp_id':'1',
                },
                {
                    'emp_id':'2'
                },
                {
                    'emp_id':'3',
                },
                { 
                    'emp_id': '4'
                }
            ]
        }
    }
)

pprint(response['Responses'])

#=============================
#GetItem

import boto3 
import pprint 

db = boto3.client('dynamodb')

response = db.get_item(
    TableName = 'Table_Name',
    Key = {
        'emp_id': {
            'S':'5'
        }
    }
)

print (response['Item'])

#============================
#Scan Table

import boto3 
import pprint  

db = boto3.resource('dynamodb')

table = db.Table('Table_Name')
response = table.scan()
data = response['Items']
pprint(data)

#=============================
#Criando uma tabela no dynamodb 
import boto3 

def create_movie_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName = 'Movies',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'title',
                'KeyType':'RANGE'
            }
        ],

        AttributeDefinitions = [ 
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            }
        ],
        PrivisonedThroughPut = {
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    return table 

if __name__ == "__main__":
    movie_table = create_movie_table()
    print ("Table Status :" , movie_table.table_status)

#==========================================
#Carregando arquivo JSON para uma tabela DynamoDB

import boto3 
import json 
import decimal

def load_movie(movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Movies')

    for movie in movies:
        year = int(movie['year'])
        title = movie[ 'title']
        print("Adding Movie : ", year, title)
        table.put_item(Item=movie)

if __name__ == "__main__":
    with open('moviedata.json') as json_file:
        movie_list = json.load(json_file, parse_float=decimal)

    load_movie(movie_list)

#=============================
#Pegando dados dos filmes

import boto3 
from pprint import pprint 
from botocore.exceptions import ClientError

def get_movie(title,year,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('Movies')

    try:
        response = table.get_item(Key={'year':year,'title':title})
    except ClientError as e:
        print(e.response[ 'Error']['Message'])
    
    else:
        return response[ 'Item']

if __name__ == "__main__":
    movie = get_movie('Nome do filme', 2012)
    if movie:
        pprint(movie)

#==================================================
#Update no arquivo de filmes

import boto3 
import pprint 
import decimal 


def update_movie(title,year,rating,plot,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    
    table =  dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'year':year,
            'title':title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p",
        ExpressionAttributeValues={
            'r':decimal(rating),
            'p': plot,
        },
        ReturnValues = 'UPDATED_NEW' 
    )

    return response

if __name__ == "__main__":
    update_response = update_movie(
        "Nome do filme", 2012, "8.1", "Updated" 
    )

    pprint(update_response)

#===========================================
#Deletando Filmes

import boto3 
import pprint 
from botocore.exceptions import ClientError

def delete_movie(title,year,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    
    table =  dynamodb.Table('Movies')

    try:
        response = table.delete_item(
            Key = {
                'year':year,
                'title':title
            }
        )
    except ClientError as e:
        print(e.response[ 'Error']['Message'])
    
    else:
        return response

if __name__ == "__main__":
    delete_response = delete_movie("nome do filme",2015)

    if delete_response:
        pprint(delete_response)

#=============================================
#Listando todos os filmes de um ano específico

import boto3 
from boto3.dynamodb.conditions import Key

def query_movies(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('Movies')
    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )

    return response['Items']

if __name__ == "__main__":
    query_year=2011
    print("Movies from {} ".format(query_year))
    
    movies = query_movies(query_year)

    for movie in movies:
        print(movie['year'], ":", movie['title'])