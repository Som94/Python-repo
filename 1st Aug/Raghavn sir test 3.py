import mysql.connector
import pandas as pd

conn=mysql.connector.connect(host='localhost',user='root',password='root',database='test',port=3306)

#query="select * from emp"
mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """
cursor=conn.cursor()
result = cursor.execute(mySql_Create_Table_Query)
conn.close()





