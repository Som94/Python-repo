import sqlalchemy
from random import randint
from datetime import datetime

import pandas as pd



name='root'            # Your MySQL User name
password='root'        # Your Password
database_name='test'   # your Database Name
engine = sqlalchemy.create_engine('mysql+pymysql://' + name + ':' + password + '@localhost:3306/' + database_name)


def valid_user():
    uid=input("Enter user id :")
    
    
    data=pd.read_sql_query("select password from User_Details where user_id={};".format(uid), engine)
    #print(data.empty)
    if data.empty:
        print("User id not matching..")
        return False
        
    else:
        psw=input('Enter apssword :') 
        if psw==str(data['password'][0]):
            return True
        else:
            print("Pasword not matching..")
            return False
    
        




