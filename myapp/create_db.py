#!usr/bin/python3
import mysql.connector 
mydb =  mysql.connector.connect(
    host="localhost",
    user="root",
    password = "FlavianLeonar2003$"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE myhomeusers")
 
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)

