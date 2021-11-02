import mysql.connector
import pandas as pd
import configparser


config_obj=configparser.ConfigParser()


config_obj.read(r'E:\Aroha Tech\Python Session\mysqwldbconfig.ini')
dbc=config_obj['mysql']

userid=dbc['user']
pwd=dbc['password']
hst=dbc['host']
db=dbc['db']
prt=dbc['port']

con=mysql.connector.connect(user=userid,password=pwd ,database=db,host=hst,port=prt)

cursor=con.cursor()


query="Show Tables"

df=pd.read_sql(query,con=con)

print(df)