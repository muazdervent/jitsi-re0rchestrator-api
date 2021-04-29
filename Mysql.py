import mysql.connector
import datetime

class Database:
  def __init__(self):
    
    self.mydb = mysql.connector.connect(
    host="111.111.111.111", #database ip address
    user="root", 
    password="root",
    port="30306",
    database="reorchestrator"
    )
    self.cursor = self.mydb.cursor()
  

  def select(self, query):
    self.cursor.execute(query)
    return self.cursor

  def insert(self, query):
    self.cursor.execute(query)
    added_row_id = self.cursor.lastrowid
    self.mydb.commit()
    return added_row_id
  
  def close(self):
    self.cursor.close()
    self.mydb.close()


"""
db = Database()

cursor = db.select("select * from sessions")



for (sessions_id, deployment_name, session_web_port, session_jvb_port, session_load,create_time) in cursor:
  print(type(session_web_port))
  

db.insert("insert into sessions (deployment_name, session_web_port, session_jvb_port,session_load) VALUES('30211','30211','30311','0')")

db.close()

time = "{:%s}".format(datetime.datetime.now())
print(time)
"""
#{}, was hired on 


