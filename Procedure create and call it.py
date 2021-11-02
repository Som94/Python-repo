import mysql.connector

con=mysql.connector.connect(user='root',password='root',database='som1',host='localhost',port=3306)

cursor=con.cursor()


# create procedure argument value

args = [102,'total']

#Call procedure 

result=cursor.callproc('uptotal',args)


import pandas as pd

df=pd.read_sql("select * from student_marks",con=con)

print(df)


args = [103,'total']

result=cursor.callproc('uptotal',args)
