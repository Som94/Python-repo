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


query="select * from guest"

sqldata=pd.read_sql(query,con=con)

print(sqldata)

print(sqldata['no_of_record'])



temp_df = pd.DataFrame(columns=['guest_name','city','phone','company','no_of_record'])

for i,row in sqldata.iterrows():
    count = 1
    while row.No_of_records >= repeatNo:
        final= final.append(records.iloc[i])
        repeatNo += 1
        
#Droping unwanted Column
final = final.drop(['No_of_records'],axis=1)

#exporting final output to excel
final.to_excel('Output.xlsx',sheet_name='output')


