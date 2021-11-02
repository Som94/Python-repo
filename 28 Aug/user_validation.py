import sqlalchemy
from random import randint
from datetime import datetime,date

import pandas as pd



name='root'            # Your MySQL User name
password='root'        # Your Password
database_name='test'   # your Database Name
engine = sqlalchemy.create_engine('mysql+pymysql://' + name + ':' + password + '@localhost:3306/' + database_name)

def valid_user():
    global uid
    uid=input("Enter user id :")
    global data  
    data=pd.read_sql_query("select * from User_Details where user_id='{}';".format(uid), engine)
    
    #print(data)
    #print(data['Password'][0])
    #print(data['status_mode'][0])
   
    if  data.empty:
        print("User id not matching..")
        return False
        
    else:
        
             
        global d
        global pw_len
    
        d=(date.today()-data['Date'][0]).days
        #print('diff :',d)
        
        pw_len=len(str(data['Password'][0]))
        #print('len of pass',pw_len)
        #print(data.empty)
        
        psw=input('Enter password :') 
        if psw==str(data['Password'][0]):
            
            #if data['Date'][0]
            
            #print("User id  and password matching..")
            if data['status_mode'][0].lower()=='active':
               #print("ALl condition saticefied")
                print("User Details :\n",data)
                #print('diff :',d)
                return True
            else:
                print("User id  and password matching but User status is in deactive mode")
                
                return False
        else:
            print("Pasword not matching..")
            return False
    







