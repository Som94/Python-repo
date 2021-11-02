import mysql.connector

user_name = input("Enter user name :")
user_password = input("Enter password :")
user_database = input("Enter database name :")
db_host = input("Enter host name : ")
port_no = int(input("Enter your port number: "))



conn=mysql.connector.connect(user= user_name ,password= user_password , database= user_database , host = db_host , port = port_no )

cursor=conn.cursor()

try:
	cursor.execute("create table test(id int)")
	print("Created successfully")
except mysql.connector.errors.ProgrammingError as e:
    print("Table Already Exists,Try another name")
    print("Error code:",e.errno)
    print("SQLSTATE value:",e.sqlstate)
    print("Error message:",e.msg)
    print("Error:",e)
    s = str(e)
    print("Error:",s)