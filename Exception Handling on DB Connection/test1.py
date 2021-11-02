import mysql.connector

try:
  cnx = mysql.connector.connect(user='root',password='root', database='test')
  cursor = cnx.cursor()
  print(cursor.execute("select * from employee;"))   # Syntax error in query
  cnx.close()
except mysql.connector.Error as err:
  print("Something went wrong: {}".format(err))