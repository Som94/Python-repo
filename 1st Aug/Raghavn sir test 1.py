import mysql.connector
import pandas as pd

conn=mysql.connector.connect(host='localhost',user='root',password='root',database='test',port=3306)
cursor=conn.cursor()
query="select * from emp"
pdf=pd.read_sql(query, con=conn)

conn.close()
print(pdf)


