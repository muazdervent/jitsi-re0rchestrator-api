
from ../MYsql import * 
import mysql.connector
f = open("database.txt","r")
query = f.read()

db = Database()
db.inser(query)
db.close()


