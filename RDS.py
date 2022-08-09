#Create MySQL Instance 
import boto3 
import pprint 

rds_client = boto3.client('rds')
response = rds_client.create_db_instance(
    DBName = "rds-01",
    DBInstanceIdentifier = "rds-01",
    AllocatedStorage = 20,
    DBInstanceClass = "db.t2.micro",
    Engine="MySQL",
    MasterUserName = "admin",
    MasterUserPassword = "admin",
    Port = 3306,
    EngineVersion = "8.0.2",
    PubliclyAccessible = False,
    StorageType = "gp2"

)
pprint(response)
#==================================
#Create MySQL DataBase

import mysql.connector as mc 

try:
    mydb = mc.connect(
        host = "rds-01.us-east-1.rds.amazonaws.com",
        user = "admin",
        password = "admin"
    )
    dbname = input("Please enter your database name: ")

    cursor = mydb.cursor()
    cursor.execute("CREATE DATABASE {}".format(dbname))
    print("DataBase created")

except mc.Error as e:
    print("Failed to create database{}".format(dbname))

#===================================
#Check DataBase Connection

try:
    mydb = mc.connect(
        host="rds-01.us-east-1.rds.amazonaws.com",
        user="admin",
        password="admin",
        database="rds-01"
    )
    print("Connection created")

except mc.Error as e:
    print("There is no connection {}".formmat(e))

#====================================
#Create MySQL Table 

import mysql.connector as mc 

try:
    mydb = mc.connect(
        host="rds-01.us-east-1.rds.amazonaws.com",
        user="admin",
        password="admin",
        database="rds-01"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE Person(id, INT, AUTO_INCREMENT, PRIMARY_KEY, name VARCHAR(255), lastname VARCHAR(255))")

    print("Table is created")
except mc.Error as e: 
    print("Failed to create  table{}".format(e))

#=======================================
#Show MySQL Tables 

import mysql.connector as mc 

try:
    mydb = mc.connect(
    host="rds-01.us-east-1.rds.amazonaws.com",
    user="admin",
    password="admin",
    database="rds-01"
    )
    
    mycursor = mydb.cursor()

    mycursor.execute("Show Tables")
    
    for table in mycursor:
        print(table)

except mc.Error as e:
    print("Can not show the Tables{}".format(e))

#========================================
#Inserting Data into MySQL DataBase

import mysql.connector as mc 

try:
    mydb = mc.connect(
        host="rds-01.us-east-1.rds.amazonaws.com",
        user="admin",
        password="admin",
        database="rds-01"
    )
    
    mycursor = mydb.cursor()
    name = input("Please enter your name: ")
    lastname = input("Please enter your lastname: ")

    query = "INSERT INTO {database} (name, lastname) VALUES(%s,%s)"
    value = (name,lastname)

    mycursor.execute(query,value)
    mydb.commit()
    print("Data Inserted")

except mc.Error as e:
    print("Failed to add data {}".format(e))

#==============================================
#Showing Data from MySQL DataBase 

import mysql.connector as mc 

try:
    dbname = input("Please enter the database name: ")
    tablename = input("Please enter the table name: ")
    
    mydb = mc.connect(
        host="rds-01.us-east-1.rds.amazonaws.com",
        user="admin",
        password="admin",
        database = dbname 
    )
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM {database}".format(tablename))
    result = mycursor.fetchall()

    for data in result:
        print(data)

except mc.Error as e:
    print("Failed to show the Data {}".format(e))
#====================================================
#Update Data

import mysql.connector as mc 

try:
    dbname = input("Please enter the database name: ")
    tablename = input("Please enter the table name: ")
    
    mydb = mc.connect(
        host="rds-01.us-east-1.rds.amazonaws.com",
        user="admin",
        password="admin",
        database = dbname 
    )

    mycursor = mydb.cursor()
    query = "UPDATE {database} SET name='updated' WHERE id='1' "
    mycursor.execute(query)
    mydb.commit()
    print(mycursor.rowcount, "record affected")

except mc.Error as e:
    print("Can not update data {}".format(e))

#====================================
#Delete MySQL Data

import mysql.connector as mc 

try:
    dbname = input("Please enter the database name: ")
    tablename = input("Please enter the table name: ")
    
    mydb = mc.connect(
        host="rds-01.us-east-1.rds.amazonaws.com",
        user="admin",
        password="admin",
        database = dbname 
    )

    mycursor = mydb.cursor()
    query = "DELETE FROM {database} WHERE id='1'"

    mycursor.execute(query)
    mydb.commit()
    print(mycursor.rowcount,"record affected")

except mc.Error as e:
    print("Can not remove data {}".format(e))

#==================================================
#Describe MySQL 

import boto3 
from pprint import pprint 

rds_client = boto3.client('rds')

response = rds_client.describe_db_instances(
    DBInstanceIdentifier = "rds-01"
)
pprint(response)

#==================================================
#Delete MySQL Instance

import boto3 

rds_client = boto3.client('rds')
response = rds_client.delete_db_instance(
    DBInstanceIdentifier = "rds-01",
    SkipFinalSnapShot = False, #True/False
    FinalDBSnapshotIdentifier = "rds-01-final-snapshot",
    DeleteAutomatedBackup = True #True/False
)

print(response)