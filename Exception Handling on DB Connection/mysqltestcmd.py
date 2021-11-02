import mysql.connector

con=mysql.connector.connect(user='root',password='root',database='test',host='localhost',port=3306)

cursor=con.cursor()

try:
	cursor.execute('create table test(id int)')
	print("Created successfully")
except mysql.connector.errors.ProgrammingError:
	print("Table Already Exists , Try another name ")