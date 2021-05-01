
from MYsql import * 
import mysql.connector
f = open("./scripts/database.txt","r")
query = f.read()
qlist = query.split(';')

db = Database()
for i in qlist:
  db.insert(i)

db.close()


