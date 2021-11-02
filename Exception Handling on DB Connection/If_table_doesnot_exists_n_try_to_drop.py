import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user='scott', database='test')
cursor = cnx.cursor()
try:
  cursor.execute("DROP TABLE spam")


except mysql.connector.Error as err:
  if err==1045:
    print('Password not provide')

  else:
    raise