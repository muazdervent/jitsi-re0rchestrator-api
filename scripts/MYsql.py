import mysql.connector 
import datetime 
class Database: 
  def __init__(self): 
    self.mydb = mysql.connector.connect( 
      host="localhost",
      user="reorch_user",
      password="root_password_123",
      port="30306",
      database="reorch"
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
 
 
 

