'''
import boto3
import pandas as pd
s3_client=boto3.client('s3')
file=s3_client.get_object(Bucket='som-aws-bucket-1',Key='Admin_userid_password.csv')
file_df=pd.read_csv(file['Body'])
user_id=file_df.iloc[0,0]
password=file_df.iloc[0,1]'''

import sqlalchemy
from random import randint
from datetime import datetime

import pandas as pd



name='root'            # Your MySQL User name
password='root'        # Your Password
database_name='test'   # your Database Name
engine = sqlalchemy.create_engine('mysql+pymysql://' + name + ':' + password + '@localhost:3306/' + database_name)

import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="root",database="test")

mycursor = conn.cursor()


class Admin:
    
    def create_new_user():
        
        new_user_id=input("Mobile Number or Email id :")
        password=str(randint(100000,999999))
        
        date_and_time=datetime.now()
        
        date=date_and_time.date()
        time=date_and_time.strftime('%H:%M:%S')
        status_mode=input("select Active/Deactive :")
        
        user_data=[new_user_id,password,date,time,status_mode]
        
        df=pd.DataFrame([user_data],columns=['User_id','Password','Date','Time','status_mode'])
        df.to_sql(name="User_Details",con=engine,if_exists='append',index=False)
        print("A new user created successfully..")
        
    def user_view():
        all_user_details = pd.read_sql_query("select * from User_Details;", engine)
        
        user_list=[]
        for user in all_user_details['User_id']:
            user_list.append(user)
        
        
        user_data=int(input("If you want to view a perticular user details press 1 \n Or for all User details press 2 :"))
        if user_data==1:
            user_id=input("Enter the user id :")
            if user_id in user_list:
                user_detail=pd.read_sql_query("select * from User_Details where User_id={};".format(user_id), engine)
                print("Here is the User details :\n",user_detail)
            else:
                print("No such user Id..")
                
        if user_data==2:
            print("The All User details :\n",all_user_details)
            
    def delete_user():
        all_user_details = pd.read_sql_query("select * from User_Details;", engine)
        
        user_list=[]
        for user in all_user_details['User_id']:
            user_list.append(user)
        
        
        user_data=int(input("If you want to delete a perticular user details press 1 \n Or delete all User press 2 :"))
        if user_data==1:
            user_id=input("Enter the user id :")
            if user_id in user_list:
                mycursor.execute("delete from User_Details where User_id={}".format(user_id))
                conn.commit()
                print("User details deleted succesfully")
            else:
                print("No such user Id..")
                
        if user_data==2:
            mycursor.execute("delete from User_Details")
            conn.commit()
            print("All User details deleted succesfully")
            
        
    def Active():
        
        all_user_details = pd.read_sql_query("select * from User_Details;", engine)
        
        user_list=[]
        for user in all_user_details['User_id']:
            user_list.append(user)
        
        
        user_data=int(input("If you want to Active a perticular user press 1 \n Or to  Active all User press 2 :"))
        if user_data==1:
            user_id=input("Enter the user id :")
            if user_id in user_list:
                                
                mycursor.execute("update User_Details set status_mode=%s  where User_id=%s",('Active',user_id))
                conn.commit()
                print("User status mode Active now , is updated succesfully")
            else:
                print("No such user Id..")
                
        if user_data==2:
            
            mycursor.execute("update User_Details set status_mode='Active' ")
            conn.commit()
            
            print("All User status mode is now in Active , Updated succesfully")
            
    
    def Deactive():
        
        all_user_details = pd.read_sql_query("select * from User_Details;", engine)
        
        user_list=[]
        for user in all_user_details['User_id']:
            user_list.append(user)
        
        
        user_data=int(input("If you want to Active a perticular user press 1 \n Or to  Active all User press 2 :"))
        if user_data==1:
            user_id=input("Enter the user id :")
            if user_id in user_list:
                                
                mycursor.execute("update User_Details set status_mode=%s  where User_id=%s",('Deactive',user_id))
                conn.commit()
                print("User status mode Deactive now , is updated succesfully")
            else:
                print("No such user Id..")
                
        if user_data==2:
            
            mycursor.execute("update User_Details set status_mode='Deactive' ")
            conn.commit()
            
            print("All User status mode  now is in Deactive , Updated succesfully")
            
